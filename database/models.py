import sqlite3


def create_profile(name_usr, profile_heading, profile_description, profile_pic_url):
    con = sqlite3.connect('schema.sql')
    cur = con.cursor()
    cur.execute('INSERT OR IGNORE INTO UserProfile (name_usr, profile_heading, profile_description, profile_pic_url) values(?,?,?,?)', (name_usr, profile_heading,profile_description,profile_pic_url))
    con.commit()
    con.close()

def create_nft(ntf_id, user_id, nft_token, nft_url):
    con = sqlite3.connect('schema.sql')
    cur = con.cursor()
    cur.execute('INSERT OR IGNORE INTO NFT (ntf_id, user_id, nft_token, nft_url) values(?,?,?,?)', (ntf_id, user_id, nft_token, nft_url))
    con.commit()
    con.close()

def get_nfts():
    con = sqlite3.connect('schema.sql')
    cur = con.cursor()
    cur.execute('SELECT * FROM NFT')
    NFTs = cur.fetchall()
    return NFTs

def create_post(post_id, user_id, title, descript, posted_at, nft_id):
    con = sqlite3.connect('schema.sql')
    cur = con.cursor()
    cur.execute('INSERT OR IGNORE INTO Post (post_id, user_id, title, descript, posted_at, nft_id)) values(?,?,?,?,?,?)', (post_id, user_id, title, descript, posted_at, nft_id)))
    con.commit()
    con.close()

def get_posts():
    con = sqlite3.connect('schema.sql')
    cur = con.cursor()
    cur.execute('SELECT * FROM Post')
    NFTposts = cur.fetchall()
    return NFTposts

def create_reply(reply_id, user_id, post_id, replied_at, reply_text):
    con = sqlite3.connect('schema.sql')
    cur = con.cursor()
    cur.execute('INSERT OR IGNORE INTO Reply (reply_id, user_id, post_id, replied_at, reply_text)) values(?,?,?,?,?)', (reply_id, user_id, post_id, replied_at, reply_text))
    con.commit()
    con.close()

def get_replies():
    con = sqlite3.connect('schema.sql')
    cur = con.cursor()
    cur.execute('SELECT * FROM Reply')
    NFTreplies = cur.fetchall()
    return NFTreplies
   
def create_follows(user_id, follows_id):
    con = sqlite3.connect('schema.sql')
    cur = con.cursor()
    cur.execute('INSERT OR IGNORE INTO Follows (user_id, follows_id)) values(?,?)', (user_id, follows_id))
    con.commit()
    con.close()

def get_followers():
    con = sqlite3.connect('schema.sql')
    cur = con.cursor()
    cur.execute('SELECT * FROM Follows')
    followers = cur.fetchall()
    return followers

def create_user(user_id, password_usr, date_joined, roles, last_login):
    con = sqlite3.connect('schema.sql')
    cur = con.cursor()
    cur.execute('INSERT OR IGNORE INTO User (user_id, password_usr, date_joined, roles, last_login)) values(?,?,?,?,?)', (user_id, password_usr, date_joined, roles, last_login))
    con.commit()
    con.close()

def get_users():
    con = sqlite3.connect('schema.sql')
    cur = con.cursor()
    cur.execute('SELECT * FROM Users')
    users = cur.fetchall()
    return users