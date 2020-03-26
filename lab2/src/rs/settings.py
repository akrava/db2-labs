# set only of client usernames, who belongs to group `user`
USERS_SET_NAME = "users"

# set only of client usernames, who belongs to group `admin`
ADMINS_SET_NAME = "admins"

# set of users, who are online
USERS_ONLINE_SET_NAME = "users_online"

# zset of active users
ACTIVE_USERS_ZSET_NAME = "active_users"

# zset of spamers
SPAMERS_ZSET_NAME = "spamers"

# next id for message
MESSAGE_NEXT_ID_NAME = "message_next_id"

# prefix for hash of message instances
MESSAGES_HASH_SET_PREFIX = "message:"

# list - message queue, which is processing by worker
MESSAGE_QUEUE_LIST_NAME = "message_queue"

# prefix for list of incoming message ids, which belongs to concrete user
USER_INCOMING_MESSAGES_LIST_PREFIX = "incoming_messages:"

# prefix for set of outcoming message ids, which belongs to concrete user
USER_OUTCOMING_MESSAGES_SET_PREFIX = "outcoming_messages:"

# set of message ids with status `created`
MESSAGE_IDS_CREATED_SET_NAME = "messages_created"

# set of message ids with status `in queue`
MESSAGE_IDS_IN_QUEUE_SET_NAME = "messages_in_queue"

# set of message ids with status `processing`
MESSAGE_IDS_PROCESSING_SET_NAME = "messages_processing"

# set of message ids with status `blocked`
MESSAGE_IDS_BLOCKED_SET_NAME = "messages_blocked"

# set of message ids with status `send`
MESSAGE_IDS_SEND_SET_NAME = "messages_send"

# set of message ids with status `delivered`
MESSAGE_IDS_DELIVERED_SET_NAME = "messages_delivered"

