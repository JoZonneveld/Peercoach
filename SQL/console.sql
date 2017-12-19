-- CREATE TABLE testTable(
--   id INTEGER PRIMARY KEY NOT NULL,
--   name VARCHAR(64)
-- );

-- CREATE TABLE testtable2(
--   id INTEGER PRIMARY KEY NOT NULL,
--   name VARCHAR(64),
--   tt_id INTEGER REFERENCES testtable
-- );


-- INSERT INTO testtable (id, name) VALUES (1, 'test1');
-- INSERT INTO testtable (id, name) VALUES (2, 'test2');
-- INSERT INTO testtable (id, name) VALUES (3, 'test3');


-- INSERT INTO testtable2 (id, name, tt_id) VALUES (1, 'test21', 3);
-- INSERT INTO testtable2 (id, name, tt_id) VALUES (2, 'test22', 1);
-- INSERT INTO testtable2 (id, name, tt_id) VALUES (3, 'test23', 2);
-- INSERT INTO testtable2 (id, name, tt_id) VALUES (4, 'test24', 2);


SELECT tt2.id, tt2.name as t2Name, t.name as tName FROM testtable2 as tt2 INNER JOIN testtable t ON tt2.tt_id = t.id;