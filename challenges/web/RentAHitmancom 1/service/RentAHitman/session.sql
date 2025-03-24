BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "targets" (
	"targetID"	INTEGER NOT NULL,
	"name"	TEXT NOT NULL,
	"location"	TEXT NOT NULL,
	"description"	TEXT NOT NULL,
	PRIMARY KEY("targetID" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "users" (
	"userId"	INTEGER NOT NULL,
	"username"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"admin"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("userId" AUTOINCREMENT)
);
INSERT OR IGNORE INTO "targets" VALUES (1,'Baba','Singapore','Created most of the Web Challenges in YBN24. 



Known to be a horrible programmer');
INSERT OR IGNORE INTO "targets" VALUES (2,'Baba''s Alter Ego','Your House','Known to stalk people. Probably stalking you rn');
INSERT OR IGNORE INTO "targets" VALUES (3,'Baba''s Social Anxiety','My House','Currently too socially awkward to ask 

other challenge creators for 

permission to use their names.

So he''s asking chatgpt to generate fake 

people.');
INSERT OR IGNORE INTO "targets" VALUES (4,'CipherMaestro','Tokyo, Japan','A cryptography enthusiast who creates mind-boggling cipher challenges.');
INSERT OR IGNORE INTO "targets" VALUES (5,'BitBreaker','Berlin, Germany','Specializes in reverse engineering challenges with intricate assembly puzzles.');
INSERT OR IGNORE INTO "targets" VALUES (6,'DataDiver','San Francisco, USA','Known for challenging participants with advanced SQL injection scenarios.');
INSERT OR IGNORE INTO "targets" VALUES (7,'NullHunter','Bangalore, India','Focuses on web application vulnerabilities with subtle parameter tampering challenges.');
INSERT OR IGNORE INTO "targets" VALUES (8,'ExploitWizard','London, UK','A penetration tester who crafts binary exploitation challenges for experts.');
INSERT OR IGNORE INTO "targets" VALUES (9,'PacketPhantom','Sydney, Australia','Loves to design packet capture challenges with hidden network secrets.');
INSERT OR IGNORE INTO "targets" VALUES (10,'ShellMaster','Seoul, South Korea','Expert in command injection and shell escape puzzles.');
INSERT OR IGNORE INTO "targets" VALUES (11,'CryptoCracker','Moscow, Russia','Enjoys creating RSA-based cryptography challenges with surprising twists.');
INSERT OR IGNORE INTO "targets" VALUES (12,'MemoryMapper','Paris, France','Designs memory forensics challenges that test advanced debugging skills.');
INSERT OR IGNORE INTO "targets" VALUES (13,'BlockChainBreaker','Singapore, Singapore','Focuses on blockchain transaction tampering and smart contract vulnerabilities.');
INSERT OR IGNORE INTO "targets" VALUES (14,'OverflowKing','New York, USA','Masters stack and buffer overflow challenges with deep technical depth.');
INSERT OR IGNORE INTO "targets" VALUES (15,'StegoArtist','Rome, Italy','Loves hiding secrets in images and audio files, crafting unique steganography puzzles.');
INSERT OR IGNORE INTO "targets" VALUES (16,'LogicLooper','Dubai, UAE','Creates logical puzzle challenges that require sharp thinking and creativity.');
INSERT OR IGNORE INTO "targets" VALUES (17,'PortScanner','Toronto, Canada','Specializes in designing challenges around port enumeration and hidden services.');
INSERT OR IGNORE INTO "targets" VALUES (18,'SocialSleuth','Buenos Aires, Argentina','Focuses on OSINT challenges that require digging through open data sources.');
INSERT OR IGNORE INTO "targets" VALUES (19,'KeyCoder','Stockholm, Sweden','Crafts key generation challenges with complex mathematical dependencies.');
INSERT OR IGNORE INTO "targets" VALUES (20,'FileForensics','Cape Town, South Africa','Loves to work on file recovery and forensic analysis challenges.');
INSERT OR IGNORE INTO "targets" VALUES (21,'QuantumQuest','Zurich, Switzerland','Explores futuristic quantum cryptography puzzles in their challenges.');
INSERT OR IGNORE INTO "targets" VALUES (22,'BugHunter','Kuala Lumpur, Malaysia','Creates challenges that emulate real-world bug bounty scenarios.');
INSERT OR IGNORE INTO "targets" VALUES (23,'CodeCrafter','Barcelona, Spain','Focuses on secure coding challenges that reveal common programming pitfalls.');
COMMIT;
