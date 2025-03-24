# Solultion
Sign a substring of the passphrase, then use hash-extender to append the rest of the passphrase to the message.

```sh
./hash_extender --data "Yes, but no, but yes, but no" --secret 32 --append "." --signature <message_signature> --format sha256
```

Flag: `YBN24{doNt_rE1NVeNT_THE_wheEL_4c1e0ebda9c334d245f8baa7500e2b67}`