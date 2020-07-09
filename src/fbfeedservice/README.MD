## Documentary for Facebook Feed Service

### Model

#### 1. Feed

|Attributes |Data Type|Description                                  |
|---        |---      |---                                          |
|id         |int      |unique identifier from Facebook (primary key)|
|full_text  |String   |full text of the post                        |
|author_name|String   |the name of the author                       |
|reactions  |int      |the number of reactions in total             |
|crawled_dt |String   |the date of the post crawled                 |
|post_dt    |String   |the date of the post published               |
|like       |int      |the number of like of the post               |
|love       |int      |the number of love of the post               |
|angry      |int      |the number of angry of the post              |
|wow        |int      |the number of wow of the post                |
|haha       |int      |the number of haha of the post               |
|sad        |int      |the number of sad of the post                |
|comment    |int      |the number of comment of the post            |
|share_count|int      |the number of share of the post              |

#### 2. Hashtag

|Attributes |Data Type|Description                                  |
|---        |---      |---                                          |
|id         |int      |auto increase field (primary key)            |
|feed_id    |int      |the id of the post                           |
|text       |String   |the hashtag                                  |

#### 3. Page

|Attributes                |Data Type|Description                                  |
|---                       |---      |---                                          |
|id                        |int      |auto increase field (primary key)            |
|author_name               |String   |the name of the author                       |
|ads                       |Boolean  |whether the page has advertisement(s)        |
|page_created_date         |String   |the date of the page created                 |
|total_number_of_manager   |int      |the number of managers of the page in total  |
|manager                   |String   |the location of the manager                  |
