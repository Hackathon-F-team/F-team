

import pymysql
from util.DB import DB

class dbConnect:
    # usersテーブルに新規レコードを作成する。
    # app.pyで作ったuserインスタンスから、ユーザー情報を取得し、DBに格納する。
    def createUser(user):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            
            # チャットルームでニックネームを表示するため、nicknameを追加。デフォルトではユーザーネームを設定。
            sql = "INSERT INTO users (uid, user_name, email, password, nickname) VALUES (%s, %s, %s, %s, %s);"
            cur.execute(sql, (user.uid, user.name, user.email, user.password, user.name))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    # サンプルアプリと同じ。
    # usersテーブルからemailが一致するユーザーのidを取得する。
    def getUserId(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT uid FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            id = cur.fetchone()
            return id
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close



    # サンプルアプリと同じ。
    # usersテーブルからemailが一致するユーザーの全情報を取得する。
    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close



    # usersテーブルからuidが一致するユーザーの全情報を取得する。
    def getUserbyUid(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE uid=%s;"
            cur.execute(sql, (uid))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close



    # usersテーブルから、全ユーザー情報を取得する。
    def getUsersAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users;"
            cur.execute(sql)
            users = cur.fetchall()
            return users
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    
    # uidを指定して、user情報を更新する。
    def updateUser(uid, newNickname, newProfile, img_path):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE users SET nickname=%s, profile=%s ,img_path=%s WHERE uid=%s;"
            cur.execute(sql, (newNickname, newProfile, img_path, uid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()



    
    # prefecturesテーブルから、全都道府県情報を取得する。
    def getPrefectureAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM prefectures;"
            cur.execute(sql)
            prefectures = cur.fetchall()
            return prefectures
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
    


    # IDが一致する都道府県の情報を取得する。
    def getPrefectureById(pref_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM prefectures WHERE id=%s;"
            cur.execute(sql, (pref_id))
            prefecture = cur.fetchone()
            return prefecture
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
    

    #　サンプルアプリと同じ。
    #　channelsテーブルから全チャンネルの情報を取得する。
    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    # 都道府県IDを指定して、該当するチャンネルの情報を取得する。
    def getChannelByPref(pref_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE pref_id=%s;"
            cur.execute(sql, (pref_id))
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    # サンプルアプリと同じ。
    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    # サンプルアプリと同じ。
    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()




    ### channelsテーブルにテーブルを追加する。
    def addChannel(uid, newChannelName, newChannelDescription, pref_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            # pref_idも入れる。
            sql = "INSERT INTO channels (uid, name, abstract, pref_id) VALUES (%s, %s, %s, %s);"
            cur.execute(sql, (uid, newChannelName, newChannelDescription, pref_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    # サンプルアプリと同じ。
    # channel_nameが一致するチャンネル情報を取得する。
    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
        except Exception as e:
            print(e + 'が発生しました')
            return None
        finally:
            cur.close()
            return channel


    # サンプルアプリと同じ。
    # チャンネルを更新する　。ただし都道府県は変更しない。
    def updateChannel(uid, newChannelName, newChannelDescription, cid):
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "UPDATE channels SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
        cur.execute(sql, (uid, newChannelName, newChannelDescription, cid))
        conn.commit()
        cur.close()


    
    # サンプルアプリと同じ。
    # チャンネルIDを指定して、テーブルを削除する。
    def deleteChannel(cid):
        try: 
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    # チャンネルIDを指定して、同チャンネルのすべてのメッセージの各種情報を取得する。 nicknameを追加した。
    def getMessageAll(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            # nicknameも取り出す。
            # ORDER BY で並び順を指定。
            sql = "SELECT id,u.uid, user_name, nickname, message, m.img_path FROM messages AS m INNER JOIN users AS u ON m.uid = u.uid WHERE cid = %s ORDER BY id;"
            cur.execute(sql, (cid))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    # サンプルアプリと同じ。
    #　メッセージテーブルにレコードを追加する。
    def createMessage(uid, cid, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
            cur.execute(sql, (uid, cid, message))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()



    #　画像投稿があった場合に、メッセージテーブルにレコードを追加する。
    def createMessageWithImg(uid, cid, img_path):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(uid, cid, img_path) VALUES(%s, %s, %s)"
            cur.execute(sql, (uid, cid, img_path))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()


    # サンプルアプリと同じ。
    #　メッセージテーブルから、IDを指定してレコードを削除する。
    def deleteMessage(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM messages WHERE id=%s;"
            cur.execute(sql, (message_id))
            conn.commit()
        except Exception as e:
            print(e + 'が発生しています')
            return None
        finally:
            cur.close()
    


    # # IDが一致する画像のパスを取得する。
    # def getImgPathbyId(id):
    #     try:
    #         conn = DB.getConnection()
    #         cur = conn.cursor()
    #         sql = "SELECT img_path FROM images WHERE id=%s;"
    #         cur.execute(sql, (id))
    #         img_path = cur.fetchone()
    #         return img_path
    #     except Exception as e:
    #         print(e + 'が発生しています')
    #         return None
    #     finally:
    #         cur.close


    # #　imagesテーブルにレコードを追加する。
    # def createImage(id, name, img_path):
    #     try:
    #         conn = DB.getConnection()
    #         cur = conn.cursor()
    #         sql = "INSERT INTO images(id, name, img_path) VALUES(%s, %s, %s)"
    #         cur.execute(sql, (id, name, img_path))
    #         conn.commit()
    #     except Exception as e:
    #         print(e + 'が発生しています')
    #         return None
    #     finally:
    #         cur.close()