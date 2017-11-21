/*
Navicat PGSQL Data Transfer

Source Server         : pg
Source Server Version : 100000
Source Host           : localhost:5432
Source Database       : jobbole
Source Schema         : public

Target Server Type    : PGSQL
Target Server Version : 100000
File Encoding         : 65001

Date: 2017-11-10 14:35:52
*/


-- ----------------------------
-- Table structure for keywords
-- ----------------------------
DROP TABLE IF EXISTS "public"."keywords";
CREATE TABLE "public"."keywords" (
"id" int4 DEFAULT nextval('keywords_id_seq'::regclass) NOT NULL,
"keyword" varchar COLLATE "default"
)
WITH (OIDS=FALSE)

;

-- ----------------------------
-- Alter Sequences Owned By 
-- ----------------------------

-- ----------------------------
-- Primary Key structure for table keywords
-- ----------------------------
ALTER TABLE "public"."keywords" ADD PRIMARY KEY ("id");
