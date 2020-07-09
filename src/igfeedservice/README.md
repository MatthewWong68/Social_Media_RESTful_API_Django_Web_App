## Documentary for Instagram Feed Service

### Model

#### 1. Post
##### - id (String, unique page link from URL) primary key
##### - full_text (String)
##### - author_name (String)
##### - crawled_dt (String)
##### - post_dt (String)
##### - like (int)
##### - comment (int)

#### 2. Page
##### - id (auto increase) primary key
##### - author_name (String)
##### - posts (int)
##### - followers (int)
##### - following (int)

#### 3. Hashtag
##### - id (auto increase) primary key
##### - feed_id (String)
##### - text (String)


|Attributes |Data Type|Description                                  |
|---        |---      |---                                          |
|id         |String   |unique page link from URL (primary key)      |
|full_text  |String   |full text of the tweet                       |
|author_name|String   |the name of the author                       |
|crawled_dt |String   |the date of the tweet crawled                |
|post_dt    |String   |the date of the tweet published              |
|like       |int      |the number of like of the tweet              |
|comment    |int      |the number of comment of the tweet           |

#### 2. Hashtag

|Attributes |Data Type|Description                                  |
|---        |---      |---                                          |
|id         |int      |auto increase field (primary key)            |
|feed_id    |int      |the id of the feed                           |
|text       |String   |the hashtag                                  |

#### 3. Page

|Attributes |Data Type|Description                                  |
|---        |---      |---                                          |
|id         |int      |auto increase field (primary key)            |
|author_name|String   |the name of the author                       |
|posts      |int      |the number of post the page has              |
|followers  |int      |the number of follower                       |
|following  |int      |the number of page it is following           |
