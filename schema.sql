drop table if exists NFT;
    create table NFT (
        ntf_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES UserProfile(user_id) ON DELETE CASCADE,
        nft_token nft_id INTEGER, -- not sure
        nft_url text NOT NULL

    );
drop table if exists Post;
    create table Post (
        post_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id text NOT NULL, 
        title text NOT NULL,
        descript text,
        posted_at TEXT DEFAULT CURRENT_TIMESTAMP,
        nft_id INTEGER,
  FOREIGN KEY(nft_id) REFERENCES NFT(nft_id) ON DELETE CASCADE
    );

drop table if exists Reply;
    create table Reply (
        reply_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id -- probably fk
        post_id INTEGER,
  FOREIGN KEY(post_id) REFERENCES Post(post_id) ON DELETE CASCADE,
        replied_at TEXT DEFAULT CURRENT_TIMESTAMP,
        reply_text text NOT NULL
    );

drop table if exists UserProfile;
    create table UserProfile (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_usr text NOT NULL,
        profile_heading text NOT NULL,
        profile_description text NOT NULL,
        profile_pic_url --not sure,
    );

drop table if exists Follows;
    create table Follows (
        user_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES UserProfile(user_id) ON DELETE CASCADE,
        follows_id INTEGER PRIMARY KEY AUTOINCREMENT,
    );
drop table if exists User;
    create table User (
        user_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES UserProfile(user_id) ON DELETE CASCADE,
        password_usr VARCHAR(255),
        date_joined TEXT DEFAULT CURRENT_TIMESTAMP,
        roles VARCHAR(255),--not sure
        last_login TEXT DEFAULT CURRENT_TIMESTAMP
    );

drop table if exists Auth;
    create table Auth (
        user_id INTEGER,
  FOREIGN KEY(user_id) REFERENCES UserProfile(user_id) ON DELETE CASCADE,
        token VARCHAR(255),
        roles VARCHAR(255)--not sure
    );



