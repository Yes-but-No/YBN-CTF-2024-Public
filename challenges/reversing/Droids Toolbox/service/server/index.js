const { initializeApp } = require("firebase-admin/app");
const express = require("express");
const admin = require("firebase-admin");
const secrets = require("./secrets.json");
const serviceAccount = require("./service-account-key.json");
const gcpServiceAccount = require("./gcp-play-integrity-apis.json");
const crypt = require("./crypt");
const google = require("googleapis");
const GoogleAuth = require("google-auth-library");
const fs = require("fs");

const firebaseApp = initializeApp({
  credential: admin.credential.cert(serviceAccount),
});
const bodyParser = require("body-parser");
const messaging = admin.messaging();

const app = express();
// app.use(bodyParser.json());

app.get("/", (req, res) => {
  res.send(
    "Yes, but no, but yes, but no, but yes, but actually no, but yes and therefore no and henceforth yes, but no but why are you still here? Go away, nothing to see here!",
  );
});

const au2 = new GoogleAuth.GoogleAuth({
  scopes: "https://www.googleapis.com/auth/playintegrity",
});

let jsonkeys = fs.readFileSync("./gcp-play-integrity-apis.json"); // Downloaded this from the service account
let ac = au2.fromJSON(JSON.parse(jsonkeys));
google.google.options({ auth: ac });
const playintegrity = google.playintegrity_v1;
const client = new playintegrity.Playintegrity({
  version: "v1",
  auth: ac,
});
async function authMyToken(token) {
  const createResponse = await client.v1.decodeIntegrityToken({
    requestBody: {
      integrityToken: token,
    },
    packageName: "dev.czlucius.droidstoolbox",
  });

  const payloadJson = createResponse.data.tokenPayloadExternal;
  console.log("the app sent us this json", payloadJson);

  return payloadJson;
}
/*
 * token payload example:
 * (emulator)
 * {
 *  requestDetails: {
 *    requestPackageName: 'dev.czlucius.droidstoolbox',
 *    timestampMillis: '1733326585361',
 *    requestHash: '14bd7c9c6ed706742727b84255c10efeb5d61940a97f8f8e0bcfd6e21e592ba6'
 *  },
 *  appIntegrity: { appRecognitionVerdict: 'UNEVALUATED' },
 *  deviceIntegrity: {},
 *  accountDetails: { appLicensingVerdict: 'UNEVALUATED' }
 * }
 *
 * (real device)
 * {
 *  requestDetails: {
 *    requestPackageName: 'dev.czlucius.droidstoolbox',
 *    timestampMillis: '1733326061632',
 *    requestHash: '5db097745600303772282ada8501bc7f18df14eacc337cf621ae2e0e6c6d760b'
 *  },
 *  appIntegrity: {
 *    appRecognitionVerdict: 'UNRECOGNIZED_VERSION',
 *    packageName: 'dev.czlucius.droidstoolbox',
 *    certificateSha256Digest: [ 'E_TD_UfJ8wkU-KhnPZSTtS4hD2ae86A8cZzPGUcQE-Q' ],
 *    versionCode: '3'
 *  },
 *  deviceIntegrity: { deviceRecognitionVerdict: [ 'MEETS_DEVICE_INTEGRITY' ] },
 *  accountDetails: { appLicensingVerdict: 'UNEVALUATED' }
 * }
 */

const appCheckVerification = async (req, res, next) => {
  const tokenPayload = await authMyToken(req.header("X-YBN-Integrity"));
  // Check MEETS_DEVICE_INTEGRITY or MEETS_STRONG_INTEGRITY
  let compliant = false;
  let signatureCompliant = false;
  // Verdict exists
  if (
    tokenPayload.deviceIntegrity?.deviceRecognitionVerdict?.includes(
      "MEETS_DEVICE_INTEGRITY",
    ) ||
    tokenPayload.deviceIntegrity?.deviceRecognitionVerdict?.includes(
      "MEETS_STRONG_INTEGRITY",
    )
  ) {
    compliant = true;
  }

  if (!compliant) {
    return res.status(403).json({ error: "Device not compliant!" });
  } else {
    req.tokenPayload = tokenPayload;
    next();
  }
};

app.post(
  "/sendAuthorizationToken",
  [bodyParser.json(), appCheckVerification],
         (req, res) => {
           // Measure to ensure only the device has the auth token
           const authToken = secrets.authorization;
           const { token } = req.body;
           if (!token) {
             return res.json({ error: "No token provided!" });
           }
           console.log("Sending auth token to device", token);
           messaging.send({
             data: {
               authToken,
               endpoint: "getauthtoken",
             },
             token,
           });
           res.send("Thank you!");
         },
);

function getAuthorization(bearer) {
  if (bearer && bearer.startsWith("Bearer ")) {
    return bearer.substring(7);
  } else {
    return null;
  }
}

const parseOptions = {
  inflate: true,
  limit: "100kb",
  type: "application/json",
};

app.post(
  "/flag",
  [bodyParser.raw(parseOptions), appCheckVerification],
         (req, res) => {
           const authToken = secrets.authorization;
           const bearerAuthorization = getAuthorization(req.headers["authorization"]);
           if (authToken !== bearerAuthorization) {
             // not equal
             // reject
             return res.status(403).json({ error: "Authorization Token invalid!" });
           }
           const hash = req.tokenPayload?.requestDetails?.requestHash;
           const rawBody = req.body; // is a buffer
           const body = rawBody.toString("utf8");
           // body's SHA256 hash must match the hash in the token
           const bodyHash = crypt.sha256(body);

           if (bodyHash !== hash) {
             return res.status(403).json({ error: "Hash mismatch!" });
           }

           const { publicKey, token } = JSON.parse(body);

           const flag = secrets.flag;
           const encryptedFlag = crypt.encryptStringWithRsaPublicKey(flag, publicKey);

           messaging.send({
             data: {
               flag: encryptedFlag,
               endpoint: "flag",
             },
             token,
           });

           return res.send("YBN24{FAKE_FLAG}");
         },
);

app.listen(10083, () => {
  console.log("Server active!");
});
