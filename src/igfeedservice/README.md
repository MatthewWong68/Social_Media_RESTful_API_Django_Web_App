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