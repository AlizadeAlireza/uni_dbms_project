"""

    this script is for our tables and work with these

"""


def create_tables():
    pass



"""
CREATE DATABASE uni;

CREATE TABLE STT (
	STID CHAR(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    STName VARCHAR(100),
    STNJR char(20),
    STDEID char(20)
);

CREATE TABLE COT (
	COID CHAR(20) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    COTitle VARCHAR(100),
    Credit INT,
    COtype CHAR(20)
);

CREATE TABLE STCOT (
	STID CHAR(10),
    COID CHAR(10),
    TR INT PRIMARY KEY,
    YRYR INT PRIMARY KEY,
    Grade Float,
    foreign key(STID) references STT(STID),
    foreign key(COID) references COT(COID)
);

CREATE TABLE PREREQ(
	COID CHAR(10),
    PRECOID CHAR(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
    foreign key(COID) references COT(COID)
);

CREATE TABLE DEPT(
	MGRID CHAR(10),
	DEID CHAR(10)  NOT NULL AUTO_INCREMENT PRIMARY KEY,
    DEtitle varchar(100),
    phone char(12),
    address varchar(200),
    foreign key(MGRID) references PROF(PRID)
    
);

CREATE TABLE PROF(
	PRID char(10) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    PRname varchar(100),
    RANKK char(20),
	DEID CHAR(10),
    foreign key (DEID) references DEPT(DEID)
);

CREATE TABLE PRCO(
	PRID char(10) PRIMARY KEY,
    COID char(10) PRIMARY KEY,
    GROUP_ID char(10) PRIMARY KEY,
    foreign key (PRID) references PROF(PRID),
    foreign key (COID) references COT(COID)
);

"""