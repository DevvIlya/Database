create table if not exists Genre (
	id serial primary key,
	Title varchar(100) not null unique
);

create table if not exists Executor (
	id serial primary key,
	Executor_Name varchar(100) not null
);

create table if not exists Genre_Executor (
    Executor_id integer references Executor(id),
    Genre_id integer references Genre(id),
    constraint Genre_Executor_pk primary key (Genre_id, Executor_id)
);

create table if not exists Album (
	id serial primary key,
	Title varchar(100) not null unique,
	Years_Of_Release varchar(100) not null
);

create table if not exists Executor_Album (
	Album_id integer references Album(id),
	Executor_id integer references Executor(id),
	constraint Executor_Album_pk primary key (Album_id, Executor_id)
);

create table if not exists Track (
	id serial primary key,
	Title varchar(100) not null unique,
	Duration varchar(100) not null,
	Album_id integer references album(id)
);

create table if not exists Collection_Of_Songs (
    id serial primary key,
    Collection_Name varchar(100) not null unique,
    Years_Of_Release integer not null
);

create table if not exists Track_Collection (
    Track_id integer references Track(id),
    Collection_Of_Songs_id integer references Collection_Of_Songs(id),
    constraint Track_Collection_pk primary key (Track_id, Collection_Of_Songs_id)
);