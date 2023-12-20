/*
 User info for call-scheduler
 User is called call-scheduler, password = "Passw0rd$1$"

 Definition of user done from root (password dbuserdbuser):
CREATE USER 'call-scheduler'@'localhost' IDENTIFIED BY 'Passw0rd$1$';
GRANT ALL PRIVILEGES ON *.* TO 'call-scheduler'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
 */

drop schema if exists PhysicianInfo;
create schema PhysicianInfo;
use PhysicianInfo;


create table Physicians(
    id INT auto_increment primary key,
    name varchar(255) not null,
    availability varchar(255) not null
);