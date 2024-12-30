CREATE TABLE IF NOT EXISTS `warns` (
  `id` int(11) NOT NULL,
  `user_id` varchar(20) NOT NULL,
  `server_id` varchar(20) NOT NULL,
  `moderator_id` varchar(20) NOT NULL,
  `reason` varchar(255) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `Users` (
  `id` integer PRIMARY KEY,
  `discordUserId` text NOT NULL,
  `discordName` text NOT NULL,
  `isVerified` boolean NOT NULL DEFAULT 0,
  `isAllied` boolean NOT NULL DEFAULT 0,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `Pad` (
  `id` integer PRIMARY KEY,
  `upgrade` text,
  `timestampWhenFree` timestamp,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `Item` (
  `id` integer PRIMARY KEY,
  `name` text NOT NULL,
  `productionTime` integer NOT NULL,
  `waitingTime` integer NOT NULL,
  `requiredPadUpgrade` text,
  /* 
  * materialCost will be a stringify JSON
  * ex: '{"am1":10,"am2":15}'
  */
  `materialCost` json NOT NULL,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `Orders` (
  `id` integer PRIMARY KEY,
  `userId` text NOT NULL,
  `discordChannelId` text NOT NULL,
  `status` text,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(userId) REFERENCES Users(id)
);

CREATE TABLE IF NOT EXISTS `OrderRow` (
  `id` integer PRIMARY KEY,
  `userId` integer NOT NULL,
  `orderId` integer NOT NULL,
  `itemId` integer NOT NULL,
  `padId` integer,
  `status` text,
  `collectedAt` timestamp,
  `createdAt` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY(userId) REFERENCES Users(id)
  FOREIGN KEY(orderId) REFERENCES Orders(id)
  FOREIGN KEY(itemId) REFERENCES Item(id)
  FOREIGN KEY(padId) REFERENCES Pad(id)
);