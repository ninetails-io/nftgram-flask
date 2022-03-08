
CREATE_SQL = {
    'users': 'INSERT INTO users(user_id, password, roles, date_joined) VALUES (?, ?, ?, ?);',
    'profiles': 'INSERT INTO profiles(user_id, name, heading, description, profile_pic_url) VALUES (?,?,?,?,?);',
}

READ_SQL = {
    'users': 'SELECT * FROM users WHERE user_id=?;',
    'profiles': 'SELECT * FROM profiles WHERE user_id=?;',
}

UPDATE_SQL = {
    'users': 'UPDATE users SET password=? WHERE user_id=?;',
    'profiles': 'UPDATE profiles SET name=?, heading=?, description=?, profile_pic_url=? WHERE user_id=?;',
}

DELETE_SQL = {
    'users': "DELETE FROM users WHERE user_id=?;",
    'profiles' : 'DELETE FROM profiles WHERE user_id=?;',
}

CREATE_TABLES_SQL = {
    "users": """
        CREATE TABLE IF NOT EXISTS users(
            user_id TEXT PRIMARY KEY, 
            password TEXT NOT NULL, 
            roles TEXT NOT NULL DEFAULT 'user', 
            date_joined Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );""",
    "profiles": """
        CREATE TABLE IF NOT EXISTS profiles(
            user_id TEXT PRIMARY KEY, 
            name TEXT NOT NULL, 
            heading TEXT NOT NULL DEFAULT '',
            description TEXT NOT NULL DEFAULT '',
            profile_pic_url TEXT NOT NULL DEFAULT '',
            CONSTRAINT fk_user 
                FOREIGN KEY (user_id) REFERENCES users(user_id) 
                ON DELETE CASCADE
        );""",
}