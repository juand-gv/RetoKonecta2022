CREATE TABLE streamingdata(
  timestamp int NOT NULL,
  rMemberUsers int NOT NULL,
  rActiveMembers int NOT NULL,
  rOnQueueUsers_INTERACTING int NOT NULL,
  rOnQueueUsers_IDLE int NOT NULL,
  rOnQueueUsers_ACW int NOT NULL,
  PRIMARY KEY (timestamp)