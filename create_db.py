#!/usr/bin/python

import sqlite3 as lite

db_name = 'testing2.db'

create_handlers_script = """
CREATE TABLE IF NOT EXISTS handlers(
    handler_id  INTEGER PRIMARY KEY,
    name        TEXT,
    surname     TEXT,
    vat         TEXT
)"""

create_principals_script = """
CREATE TABLE IF NOT EXISTS principals(
    principal_id  INTEGER PRIMARY KEY, 
    name          TEXT,
    surname       TEXT,
    vat           TEXT,
    handled_by    INTEGER,
    FOREIGN KEY(handled_by) REFERENCES handlers(handler_id)
)"""

create_litigations_script = """
CREATE TABLE IF NOT EXISTS litigations(
    litigation_id  INTEGER PRIMARY KEY,
    hearing_day    TEXT,
    owned_by       INTEGER,
    FOREIGN KEY(owned_by) REFERENCES principals(principal_id)
)"""

create_procedures_script = """
CREATE TABLE IF NOT EXISTS procedures(
    procedure_id  INTEGER PRIMARY KEY,
    kind          TEXT,
    procedure_of  INTEGER,
    FOREIGN KEY(procedure_of) REFERENCES litigations(litigation_id)
)"""

create_deadlines_script = """
CREATE TABLE IF NOT EXISTS deadlines(
    deadline_id  INTEGER PRIMARY KEY,
    date_of         TEXT,
    expired      TEXT,
    deadline_of  INTEGER,
    FOREIGN KEY(deadline_of) REFERENCES procedures(procedure_id)
)"""

conn = lite.connect(db_name)

with conn:
    
    cur = conn.cursor()
    cur.execute(create_handlers_script)
    cur.execute(create_principals_script)
    cur.execute(create_litigations_script)
    cur.execute(create_procedures_script)
    cur.execute(create_deadlines_script)
    

