## Documentary for Facebook Feed Service

### Model

#### 1. Feed
##### - id (int, unique identifier from Facebook) primary key
##### - full_text (String)
##### - author_name (String)
##### - reactions (int)
##### - crawled_dt (String)
##### - post_dt (String)
##### - like (int)
##### - love (int)
##### - angry (int)
##### - wow (int)
##### - haha (int)
##### - sad (int)
##### - comment (int)
##### - share_count (int)

#### 2. Hashtag
##### - id (auto increase) primary key
##### - feed_id (int)
##### - text (String) 

#### 3. Page
##### - id (auto increase) primary key
##### - author_name (String)
##### - ads (Boolean)
##### - page_created_date (String)
##### - total_number_of_manager (int)
##### - manager (String)