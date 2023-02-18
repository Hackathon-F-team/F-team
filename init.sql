
-- DROP文は存在しないものを削除しようとするとエラーが出るため、IF EXISTSを追加してエラーを回避。
-- 存在する場合は、chatappと'testuser'@'localhost'を削除する。
DROP DATABASE IF EXISTS mapchat;
DROP USER IF EXISTS 'testuser'@'localhost';


CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';

-- データベース mapchat　を作成する。
CREATE DATABASE mapchat;
USE mapchat
GRANT ALL PRIVILEGES ON mapchat.* TO 'testuser'@'localhost';



-- usersテーブルを作成する。
CREATE TABLE users (
    uid varchar(255) PRIMARY KEY,
    user_name varchar(255) UNIQUE NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL,
    nickname varchar(255),
    profile text,
    -- varchar型に変更
    img_id varchar(255)
);


-- channelsテーブルを作成する。
CREATE TABLE channels (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    name varchar(255) UNIQUE NOT NULL,
    abstract varchar(255),
    pref_id int unsigned NOT NULL
);


-- messagesテーブルを作成する。
-- 外部キー制約を追加。
CREATE TABLE messages (
    id serial PRIMARY KEY,
    uid varchar(255),
    -- channelsテーブルのidと型を揃えるため、 bigint unsigned を設定。
    -- DESC channels; で型の確認ができる。
    cid bigint unsigned not null,
    message text,
    created_at timestamp not null default current_timestamp,
    -- varchar型に変更
    img_id varchar(255),
	
	-- 外部キー制約。channelsテーブルのidを参照し、チャンネルが削除された際には、同チャンネル内のメッセージのレコードも削除する。
	INDEX cid_index (cid),
	FOREIGN KEY fk_cid (cid)
		REFERENCES channels(id)
		ON DELETE CASCADE
);





-- prefecturesテーブルを作成する。
CREATE TABLE prefectures (
    id int unsigned PRIMARY KEY,
    name_jp varchar(255) UNIQUE NOT NULL,
    name_en varchar(255) UNIQUE NOT NULL
);


-- reactionsテーブルを作成する。
CREATE TABLE reactions (
    mes_id bigint unsigned NOT NULL,
    uid varchar(255) NOT NULL,
    good bit(1),
    thanks bit(1),
    god bit(1),
    PRIMARY KEY(mes_id, uid)
);


-- imagesテーブルを作成する。
CREATE TABLE images (
    id varchar(255) PRIMARY KEY,
    name varchar(255),
    img_path varchar(255) UNIQUE NOT NULL
);






-- テーブルにレコードの例を登録する。
INSERT INTO users(uid, user_name, email, password, nickname, profile)VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト','test@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578','ニックネーム','プロフィール');
INSERT INTO channels(id, uid, name, abstract, pref_id)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','富良野のレストラン情報','富良野最高！','1');
INSERT INTO channels(id, uid, name, abstract, pref_id)VALUES(2, '970af84c-dd40-47ff-af23-282b72b7cca8','どこでキツネ見られますか？','イルカも見たいです','1');
INSERT INTO channels(id, uid, name, abstract, pref_id)VALUES(3, '970af84c-dd40-47ff-af23-282b72b7cca8','津軽のグルメ','青森最高！','2');
INSERT INTO messages(id, uid, cid, message)VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8', '1', '景色いいところありますか？');
INSERT INTO messages(id, uid, cid, message)VALUES(2, '970af84c-dd40-47ff-af23-282b72b7cca8', '2', 'キタキツネかわいい');
INSERT INTO messages(id, uid, cid, message)VALUES(3, '970af84c-dd40-47ff-af23-282b72b7cca8', '3', '津軽最高！');


-- ４７都道府県のレコードを登録する。
INSERT INTO prefectures (id, name_jp, name_en)
VALUES
(1, '北海道', 'Hokkaido'),
(2, '青森県', 'Aomori'),
(3, '岩手県', 'Iwate'),
(4, '宮城県', 'Miyagi'),
(5, '秋田県', 'Akita'),
(6, '山形県', 'Yamagata'),
(7, '福島県', 'Fukushima'),
(8,  '茨城県', 'Ibaraki'),
(9, '栃木県', 'Tochigi'),
(10, '群馬県', 'Gumma'),
(11, '埼玉県', 'Saitama'),
(12, '千葉県', 'Chiba'),
(13, '東京都', 'Tokyo'),
(14, '神奈川県', 'Kanagawa'),
(15, '新潟県', 'Niigata'),
(16, '富山県', 'Toyama'),
(17, '石川県', 'Ishikawa'),
(18, '福井県', 'Fukui'),
(19, '山梨県', 'Yamanashi'),
(20, '長野県', 'Nagano'),
(21, '岐阜県', 'Gifu'),
(22, '静岡県', 'Shizuoka'),
(23, '愛知県', 'Aichi'),
(24, '三重県', 'Mie'),
(25, '滋賀県', 'Shiga'),
(26, '京都府', 'Kyoto'),
(27, '大阪府', 'Osaka'),
(28, '兵庫県', 'Hyogo'),
(29, '奈良県', 'Nara'),
(30, '和歌山県', 'Wakayama'),
(31, '鳥取県', 'Tottori'),
(32, '島根県', 'Shimane'),
(33, '岡山県', 'Okayama'),
(34, '広島県', 'Hiroshima'),
(35, '山口県', 'Yamaguchi'),
(36, '徳島県', 'Tokushima'),
(37, '香川県', 'Kagawa'),
(38, '愛媛県', 'Ehime'),
(39, '高知県', 'Kochi'),
(40, '福岡県', 'Fukuoka'),
(41, '佐賀県', 'Saga'),
(42, '長崎県', 'Nagasaki'),
(43, '熊本県', 'Kumamoto'),
(44, '大分県', 'Oita'),
(45, '宮崎県', 'Miyazaki'),
(46, '鹿児島県', 'Kagoshima'),
(47, '沖縄県', 'Okinawa');


