drop table if exists nbastats;
create table nbastats (
    id integer primary key autoincrement,
    name varchar,
    date varchar,
    team varchar,
    opposite_team varchar,
    points_made integer
);
