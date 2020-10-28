{
 "cells": [
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "We will collect text data using Twitter API."
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "!pip install tweepy"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "!pip install openpyxl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import tweepy\n",
    "import json\n",
    "from tweepy import OAuthHandler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "consumer_key = \"LzsCOl12ZZ79FObx7BV9a1R3a\"\n",
    "consumer_secret = \"gODxZ1kHJHDGgYfyP12AUN37UTlDd6yn3OsSV9Tl0iwu0K0cRY\"\n",
    "access_token = \"296102538-kYIK8SULCmRK4vgvYD2DhKbwvSXrgTdTkWh0Nvsp\"\n",
    "access_token_secret = \"Ib9obwgcE5tZk4S6tY5rAqI5iXOeJc9FGFg28qHoa4YpP\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "auth = tweepy.OAuthHandler( consumer_key , consumer_secret )\n",
    "auth.set_access_token( access_token , access_token_secret )\n",
    "api = tweepy.API(auth)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "query = \"RCB winning IPL\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Status(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'created_at': 'Wed Oct 28 12:55:16 +0000 2020', 'id': 1321435363244609536, 'id_str': '1321435363244609536', 'full_text': 'RCB have lacked with bowling combinations in the past editions of the IPL. This time they have one of the best T20 bowlers in their lineup. Can they go all the way this time after winning today &amp; qualifying?\\n@unacademy #UnacademyAskTheExperts @DisneyplusHSVIP', 'truncated': False, 'display_text_range': [0, 263], 'entities': {'hashtags': [{'text': 'UnacademyAskTheExperts', 'indices': [223, 246]}], 'symbols': [], 'user_mentions': [{'screen_name': 'unacademy', 'name': 'Unacademy', 'id': 231029978, 'id_str': '231029978', 'indices': [212, 222]}, {'screen_name': 'DisneyplusHSVIP', 'name': 'Disney+HotstarVIP', 'id': 1102821358734635008, 'id_str': '1102821358734635008', 'indices': [247, 263]}], 'urls': []}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 2938385856, 'id_str': '2938385856', 'name': 'Moin Ali', 'screen_name': 'moinali786', 'location': 'Bengaluru South, India', 'description': 'When going gets tough, the tough gets going\\nRCBian™ ✌', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 459, 'friends_count': 270, 'listed_count': 2, 'created_at': 'Sun Dec 21 16:14:42 +0000 2014', 'favourites_count': 809, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': False, 'statuses_count': 419, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1283313930803146752/cCS-LyzX_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1283313930803146752/cCS-LyzX_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2938385856/1602171130', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 10, 28, 12, 55, 16), id=1321435363244609536, id_str='1321435363244609536', full_text='RCB have lacked with bowling combinations in the past editions of the IPL. This time they have one of the best T20 bowlers in their lineup. Can they go all the way this time after winning today &amp; qualifying?\\n@unacademy #UnacademyAskTheExperts @DisneyplusHSVIP', truncated=False, display_text_range=[0, 263], entities={'hashtags': [{'text': 'UnacademyAskTheExperts', 'indices': [223, 246]}], 'symbols': [], 'user_mentions': [{'screen_name': 'unacademy', 'name': 'Unacademy', 'id': 231029978, 'id_str': '231029978', 'indices': [212, 222]}, {'screen_name': 'DisneyplusHSVIP', 'name': 'Disney+HotstarVIP', 'id': 1102821358734635008, 'id_str': '1102821358734635008', 'indices': [247, 263]}], 'urls': []}, metadata={'iso_language_code': 'en', 'result_type': 'recent'}, source='Twitter for Android', source_url='http://twitter.com/download/android', in_reply_to_status_id=None, in_reply_to_status_id_str=None, in_reply_to_user_id=None, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, author=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 2938385856, 'id_str': '2938385856', 'name': 'Moin Ali', 'screen_name': 'moinali786', 'location': 'Bengaluru South, India', 'description': 'When going gets tough, the tough gets going\\nRCBian™ ✌', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 459, 'friends_count': 270, 'listed_count': 2, 'created_at': 'Sun Dec 21 16:14:42 +0000 2014', 'favourites_count': 809, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': False, 'statuses_count': 419, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1283313930803146752/cCS-LyzX_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1283313930803146752/cCS-LyzX_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2938385856/1602171130', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=2938385856, id_str='2938385856', name='Moin Ali', screen_name='moinali786', location='Bengaluru South, India', description='When going gets tough, the tough gets going\\nRCBian™ ✌', url=None, entities={'description': {'urls': []}}, protected=False, followers_count=459, friends_count=270, listed_count=2, created_at=datetime.datetime(2014, 12, 21, 16, 14, 42), favourites_count=809, utc_offset=None, time_zone=None, geo_enabled=True, verified=False, statuses_count=419, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='C0DEED', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1283313930803146752/cCS-LyzX_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1283313930803146752/cCS-LyzX_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/2938385856/1602171130', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=False, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), user=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 2938385856, 'id_str': '2938385856', 'name': 'Moin Ali', 'screen_name': 'moinali786', 'location': 'Bengaluru South, India', 'description': 'When going gets tough, the tough gets going\\nRCBian™ ✌', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 459, 'friends_count': 270, 'listed_count': 2, 'created_at': 'Sun Dec 21 16:14:42 +0000 2014', 'favourites_count': 809, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': False, 'statuses_count': 419, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1283313930803146752/cCS-LyzX_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1283313930803146752/cCS-LyzX_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2938385856/1602171130', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=2938385856, id_str='2938385856', name='Moin Ali', screen_name='moinali786', location='Bengaluru South, India', description='When going gets tough, the tough gets going\\nRCBian™ ✌', url=None, entities={'description': {'urls': []}}, protected=False, followers_count=459, friends_count=270, listed_count=2, created_at=datetime.datetime(2014, 12, 21, 16, 14, 42), favourites_count=809, utc_offset=None, time_zone=None, geo_enabled=True, verified=False, statuses_count=419, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='C0DEED', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1283313930803146752/cCS-LyzX_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1283313930803146752/cCS-LyzX_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/2938385856/1602171130', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=False, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=0, favorited=False, retweeted=False, lang='en') \n",
      "\n",
      ".....................................\n",
      "\n",
      "Status(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'created_at': 'Wed Oct 28 12:19:47 +0000 2020', 'id': 1321426432417959937, 'id_str': '1321426432417959937', 'full_text': \"Who will win today's IPL match MI vs RCB?\\nIt’s winning time!!! Take participation in our daily quiz and get a chance to win a bat or ball.\\nNote: The lucky winner will be announced after the IPL\\n#cricket #cricketfans  #IPL2020  \\n#Contest #DailyQuiz\\n#IPL13  #criconetonline.com https://t.co/YxKwRLsQYu\", 'truncated': False, 'display_text_range': [0, 275], 'entities': {'hashtags': [{'text': 'cricket', 'indices': [194, 202]}, {'text': 'cricketfans', 'indices': [203, 215]}, {'text': 'IPL2020', 'indices': [217, 225]}, {'text': 'Contest', 'indices': [228, 236]}, {'text': 'DailyQuiz', 'indices': [237, 247]}, {'text': 'IPL13', 'indices': [248, 254]}, {'text': 'criconetonline', 'indices': [256, 271]}], 'symbols': [], 'user_mentions': [], 'urls': [], 'media': [{'id': 1321426371927629824, 'id_str': '1321426371927629824', 'indices': [276, 299], 'media_url': 'http://pbs.twimg.com/media/ElamSLeUYAADUPk.jpg', 'media_url_https': 'https://pbs.twimg.com/media/ElamSLeUYAADUPk.jpg', 'url': 'https://t.co/YxKwRLsQYu', 'display_url': 'pic.twitter.com/YxKwRLsQYu', 'expanded_url': 'https://twitter.com/criconetonline/status/1321426432417959937/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'small': {'w': 680, 'h': 340, 'resize': 'fit'}, 'medium': {'w': 1024, 'h': 512, 'resize': 'fit'}, 'large': {'w': 1024, 'h': 512, 'resize': 'fit'}}}]}, 'extended_entities': {'media': [{'id': 1321426371927629824, 'id_str': '1321426371927629824', 'indices': [276, 299], 'media_url': 'http://pbs.twimg.com/media/ElamSLeUYAADUPk.jpg', 'media_url_https': 'https://pbs.twimg.com/media/ElamSLeUYAADUPk.jpg', 'url': 'https://t.co/YxKwRLsQYu', 'display_url': 'pic.twitter.com/YxKwRLsQYu', 'expanded_url': 'https://twitter.com/criconetonline/status/1321426432417959937/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'small': {'w': 680, 'h': 340, 'resize': 'fit'}, 'medium': {'w': 1024, 'h': 512, 'resize': 'fit'}, 'large': {'w': 1024, 'h': 512, 'resize': 'fit'}}}]}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 869781347442634752, 'id_str': '869781347442634752', 'name': 'Criconet', 'screen_name': 'criconetonline', 'location': 'Gurgaon, India', 'description': 'Criconet is a social site for cricket fans and a platform for coaching and live screening of club and local matches', 'url': 'https://t.co/6R82LNjkR2', 'entities': {'url': {'urls': [{'url': 'https://t.co/6R82LNjkR2', 'expanded_url': 'http://criconetonline.com', 'display_url': 'criconetonline.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 84, 'friends_count': 493, 'listed_count': 1, 'created_at': 'Wed May 31 05:03:27 +0000 2017', 'favourites_count': 1010, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 1965, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1291675457398566912/YiJgwtkk_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1291675457398566912/YiJgwtkk_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/869781347442634752/1596779375', 'profile_link_color': '1B95E0', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 1, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 10, 28, 12, 19, 47), id=1321426432417959937, id_str='1321426432417959937', full_text=\"Who will win today's IPL match MI vs RCB?\\nIt’s winning time!!! Take participation in our daily quiz and get a chance to win a bat or ball.\\nNote: The lucky winner will be announced after the IPL\\n#cricket #cricketfans  #IPL2020  \\n#Contest #DailyQuiz\\n#IPL13  #criconetonline.com https://t.co/YxKwRLsQYu\", truncated=False, display_text_range=[0, 275], entities={'hashtags': [{'text': 'cricket', 'indices': [194, 202]}, {'text': 'cricketfans', 'indices': [203, 215]}, {'text': 'IPL2020', 'indices': [217, 225]}, {'text': 'Contest', 'indices': [228, 236]}, {'text': 'DailyQuiz', 'indices': [237, 247]}, {'text': 'IPL13', 'indices': [248, 254]}, {'text': 'criconetonline', 'indices': [256, 271]}], 'symbols': [], 'user_mentions': [], 'urls': [], 'media': [{'id': 1321426371927629824, 'id_str': '1321426371927629824', 'indices': [276, 299], 'media_url': 'http://pbs.twimg.com/media/ElamSLeUYAADUPk.jpg', 'media_url_https': 'https://pbs.twimg.com/media/ElamSLeUYAADUPk.jpg', 'url': 'https://t.co/YxKwRLsQYu', 'display_url': 'pic.twitter.com/YxKwRLsQYu', 'expanded_url': 'https://twitter.com/criconetonline/status/1321426432417959937/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'small': {'w': 680, 'h': 340, 'resize': 'fit'}, 'medium': {'w': 1024, 'h': 512, 'resize': 'fit'}, 'large': {'w': 1024, 'h': 512, 'resize': 'fit'}}}]}, extended_entities={'media': [{'id': 1321426371927629824, 'id_str': '1321426371927629824', 'indices': [276, 299], 'media_url': 'http://pbs.twimg.com/media/ElamSLeUYAADUPk.jpg', 'media_url_https': 'https://pbs.twimg.com/media/ElamSLeUYAADUPk.jpg', 'url': 'https://t.co/YxKwRLsQYu', 'display_url': 'pic.twitter.com/YxKwRLsQYu', 'expanded_url': 'https://twitter.com/criconetonline/status/1321426432417959937/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'small': {'w': 680, 'h': 340, 'resize': 'fit'}, 'medium': {'w': 1024, 'h': 512, 'resize': 'fit'}, 'large': {'w': 1024, 'h': 512, 'resize': 'fit'}}}]}, metadata={'iso_language_code': 'en', 'result_type': 'recent'}, source='Twitter Web App', source_url='https://mobile.twitter.com', in_reply_to_status_id=None, in_reply_to_status_id_str=None, in_reply_to_user_id=None, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, author=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 869781347442634752, 'id_str': '869781347442634752', 'name': 'Criconet', 'screen_name': 'criconetonline', 'location': 'Gurgaon, India', 'description': 'Criconet is a social site for cricket fans and a platform for coaching and live screening of club and local matches', 'url': 'https://t.co/6R82LNjkR2', 'entities': {'url': {'urls': [{'url': 'https://t.co/6R82LNjkR2', 'expanded_url': 'http://criconetonline.com', 'display_url': 'criconetonline.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 84, 'friends_count': 493, 'listed_count': 1, 'created_at': 'Wed May 31 05:03:27 +0000 2017', 'favourites_count': 1010, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 1965, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1291675457398566912/YiJgwtkk_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1291675457398566912/YiJgwtkk_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/869781347442634752/1596779375', 'profile_link_color': '1B95E0', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=869781347442634752, id_str='869781347442634752', name='Criconet', screen_name='criconetonline', location='Gurgaon, India', description='Criconet is a social site for cricket fans and a platform for coaching and live screening of club and local matches', url='https://t.co/6R82LNjkR2', entities={'url': {'urls': [{'url': 'https://t.co/6R82LNjkR2', 'expanded_url': 'http://criconetonline.com', 'display_url': 'criconetonline.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=84, friends_count=493, listed_count=1, created_at=datetime.datetime(2017, 5, 31, 5, 3, 27), favourites_count=1010, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=1965, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='000000', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1291675457398566912/YiJgwtkk_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1291675457398566912/YiJgwtkk_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/869781347442634752/1596779375', profile_link_color='1B95E0', profile_sidebar_border_color='000000', profile_sidebar_fill_color='000000', profile_text_color='000000', profile_use_background_image=False, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), user=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 869781347442634752, 'id_str': '869781347442634752', 'name': 'Criconet', 'screen_name': 'criconetonline', 'location': 'Gurgaon, India', 'description': 'Criconet is a social site for cricket fans and a platform for coaching and live screening of club and local matches', 'url': 'https://t.co/6R82LNjkR2', 'entities': {'url': {'urls': [{'url': 'https://t.co/6R82LNjkR2', 'expanded_url': 'http://criconetonline.com', 'display_url': 'criconetonline.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 84, 'friends_count': 493, 'listed_count': 1, 'created_at': 'Wed May 31 05:03:27 +0000 2017', 'favourites_count': 1010, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 1965, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1291675457398566912/YiJgwtkk_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1291675457398566912/YiJgwtkk_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/869781347442634752/1596779375', 'profile_link_color': '1B95E0', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=869781347442634752, id_str='869781347442634752', name='Criconet', screen_name='criconetonline', location='Gurgaon, India', description='Criconet is a social site for cricket fans and a platform for coaching and live screening of club and local matches', url='https://t.co/6R82LNjkR2', entities={'url': {'urls': [{'url': 'https://t.co/6R82LNjkR2', 'expanded_url': 'http://criconetonline.com', 'display_url': 'criconetonline.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=84, friends_count=493, listed_count=1, created_at=datetime.datetime(2017, 5, 31, 5, 3, 27), favourites_count=1010, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=1965, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='000000', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1291675457398566912/YiJgwtkk_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1291675457398566912/YiJgwtkk_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/869781347442634752/1596779375', profile_link_color='1B95E0', profile_sidebar_border_color='000000', profile_sidebar_fill_color='000000', profile_text_color='000000', profile_use_background_image=False, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=1, favorited=False, retweeted=False, possibly_sensitive=False, lang='en') \n",
      "\n",
      ".....................................\n",
      "\n",
      "Status(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'created_at': 'Wed Oct 28 12:08:08 +0000 2020', 'id': 1321423503501877248, 'id_str': '1321423503501877248', 'full_text': \"Both MI and RCB will be looking to secure their spot in the IPL playoffs by winning today's match. Who do you think will win?\\n\\n@mipaltan @RCBTweets \\n\\n#MumbaiIndians #MIvRCB #RCB #IPL2020\", 'truncated': False, 'display_text_range': [0, 186], 'entities': {'hashtags': [{'text': 'MumbaiIndians', 'indices': [150, 164]}, {'text': 'MIvRCB', 'indices': [165, 172]}, {'text': 'RCB', 'indices': [173, 177]}, {'text': 'IPL2020', 'indices': [178, 186]}], 'symbols': [], 'user_mentions': [{'screen_name': 'mipaltan', 'name': 'Mumbai Indians', 'id': 106345557, 'id_str': '106345557', 'indices': [127, 136]}, {'screen_name': 'RCBTweets', 'name': 'Royal Challengers Bangalore', 'id': 70931004, 'id_str': '70931004', 'indices': [137, 147]}], 'urls': []}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 742293662638309376, 'id_str': '742293662638309376', 'name': 'Mumbai Live', 'screen_name': 'MumbaiLiveNews', 'location': 'Mumbai, India', 'description': 'Bringing everything Mumbai #ForYou', 'url': 'https://t.co/lmYccR0cfp', 'entities': {'url': {'urls': [{'url': 'https://t.co/lmYccR0cfp', 'expanded_url': 'http://www.mumbailive.com', 'display_url': 'mumbailive.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 13507, 'friends_count': 458, 'listed_count': 68, 'created_at': 'Mon Jun 13 09:52:55 +0000 2016', 'favourites_count': 1681, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': False, 'statuses_count': 24714, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1278264507903512578/AX4BzBK-_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1278264507903512578/AX4BzBK-_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/742293662638309376/1586238887', 'profile_link_color': '19232D', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 3, 'favorited': False, 'retweeted': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 10, 28, 12, 8, 8), id=1321423503501877248, id_str='1321423503501877248', full_text=\"Both MI and RCB will be looking to secure their spot in the IPL playoffs by winning today's match. Who do you think will win?\\n\\n@mipaltan @RCBTweets \\n\\n#MumbaiIndians #MIvRCB #RCB #IPL2020\", truncated=False, display_text_range=[0, 186], entities={'hashtags': [{'text': 'MumbaiIndians', 'indices': [150, 164]}, {'text': 'MIvRCB', 'indices': [165, 172]}, {'text': 'RCB', 'indices': [173, 177]}, {'text': 'IPL2020', 'indices': [178, 186]}], 'symbols': [], 'user_mentions': [{'screen_name': 'mipaltan', 'name': 'Mumbai Indians', 'id': 106345557, 'id_str': '106345557', 'indices': [127, 136]}, {'screen_name': 'RCBTweets', 'name': 'Royal Challengers Bangalore', 'id': 70931004, 'id_str': '70931004', 'indices': [137, 147]}], 'urls': []}, metadata={'iso_language_code': 'en', 'result_type': 'recent'}, source='Twitter for iPhone', source_url='http://twitter.com/download/iphone', in_reply_to_status_id=None, in_reply_to_status_id_str=None, in_reply_to_user_id=None, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, author=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 742293662638309376, 'id_str': '742293662638309376', 'name': 'Mumbai Live', 'screen_name': 'MumbaiLiveNews', 'location': 'Mumbai, India', 'description': 'Bringing everything Mumbai #ForYou', 'url': 'https://t.co/lmYccR0cfp', 'entities': {'url': {'urls': [{'url': 'https://t.co/lmYccR0cfp', 'expanded_url': 'http://www.mumbailive.com', 'display_url': 'mumbailive.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 13507, 'friends_count': 458, 'listed_count': 68, 'created_at': 'Mon Jun 13 09:52:55 +0000 2016', 'favourites_count': 1681, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': False, 'statuses_count': 24714, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1278264507903512578/AX4BzBK-_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1278264507903512578/AX4BzBK-_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/742293662638309376/1586238887', 'profile_link_color': '19232D', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=742293662638309376, id_str='742293662638309376', name='Mumbai Live', screen_name='MumbaiLiveNews', location='Mumbai, India', description='Bringing everything Mumbai #ForYou', url='https://t.co/lmYccR0cfp', entities={'url': {'urls': [{'url': 'https://t.co/lmYccR0cfp', 'expanded_url': 'http://www.mumbailive.com', 'display_url': 'mumbailive.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=13507, friends_count=458, listed_count=68, created_at=datetime.datetime(2016, 6, 13, 9, 52, 55), favourites_count=1681, utc_offset=None, time_zone=None, geo_enabled=True, verified=False, statuses_count=24714, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='000000', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1278264507903512578/AX4BzBK-_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1278264507903512578/AX4BzBK-_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/742293662638309376/1586238887', profile_link_color='19232D', profile_sidebar_border_color='000000', profile_sidebar_fill_color='000000', profile_text_color='000000', profile_use_background_image=False, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), user=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 742293662638309376, 'id_str': '742293662638309376', 'name': 'Mumbai Live', 'screen_name': 'MumbaiLiveNews', 'location': 'Mumbai, India', 'description': 'Bringing everything Mumbai #ForYou', 'url': 'https://t.co/lmYccR0cfp', 'entities': {'url': {'urls': [{'url': 'https://t.co/lmYccR0cfp', 'expanded_url': 'http://www.mumbailive.com', 'display_url': 'mumbailive.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 13507, 'friends_count': 458, 'listed_count': 68, 'created_at': 'Mon Jun 13 09:52:55 +0000 2016', 'favourites_count': 1681, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': False, 'statuses_count': 24714, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1278264507903512578/AX4BzBK-_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1278264507903512578/AX4BzBK-_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/742293662638309376/1586238887', 'profile_link_color': '19232D', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=742293662638309376, id_str='742293662638309376', name='Mumbai Live', screen_name='MumbaiLiveNews', location='Mumbai, India', description='Bringing everything Mumbai #ForYou', url='https://t.co/lmYccR0cfp', entities={'url': {'urls': [{'url': 'https://t.co/lmYccR0cfp', 'expanded_url': 'http://www.mumbailive.com', 'display_url': 'mumbailive.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=13507, friends_count=458, listed_count=68, created_at=datetime.datetime(2016, 6, 13, 9, 52, 55), favourites_count=1681, utc_offset=None, time_zone=None, geo_enabled=True, verified=False, statuses_count=24714, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='000000', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1278264507903512578/AX4BzBK-_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1278264507903512578/AX4BzBK-_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/742293662638309376/1586238887', profile_link_color='19232D', profile_sidebar_border_color='000000', profile_sidebar_fill_color='000000', profile_text_color='000000', profile_use_background_image=False, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=3, favorited=False, retweeted=False, lang='en') \n",
      "\n",
      ".....................................\n",
      "\n",
      "Status(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'created_at': 'Wed Oct 28 11:54:07 +0000 2020', 'id': 1321419976712974336, 'id_str': '1321419976712974336', 'full_text': 'MI vs RCB Dream11 Winning Team Prediction\\n\\nVisit : https://t.co/xi0XoleJB7\\n\\n#Dream11IPL #Dream11 #Dream11Team #dream11Prediction #Dream11IPL2020 #Dream11Tips #IPL2020 #IPLinUAE #IPL #IPLT20 #MI #RCB #MIvsRCB #MIvRCB #RCBvMI #RCBvsMI #ViratKohli #HITMAN #RohitSharma #MumbaiIndians https://t.co/amAsv1iUk6', 'truncated': False, 'display_text_range': [0, 280], 'entities': {'hashtags': [{'text': 'Dream11IPL', 'indices': [76, 87]}, {'text': 'Dream11', 'indices': [88, 96]}, {'text': 'Dream11Team', 'indices': [97, 109]}, {'text': 'dream11Prediction', 'indices': [110, 128]}, {'text': 'Dream11IPL2020', 'indices': [129, 144]}, {'text': 'Dream11Tips', 'indices': [145, 157]}, {'text': 'IPL2020', 'indices': [158, 166]}, {'text': 'IPLinUAE', 'indices': [167, 176]}, {'text': 'IPL', 'indices': [177, 181]}, {'text': 'IPLT20', 'indices': [182, 189]}, {'text': 'MI', 'indices': [190, 193]}, {'text': 'RCB', 'indices': [194, 198]}, {'text': 'MIvsRCB', 'indices': [199, 207]}, {'text': 'MIvRCB', 'indices': [208, 215]}, {'text': 'RCBvMI', 'indices': [216, 223]}, {'text': 'RCBvsMI', 'indices': [224, 232]}, {'text': 'ViratKohli', 'indices': [233, 244]}, {'text': 'HITMAN', 'indices': [245, 252]}, {'text': 'RohitSharma', 'indices': [253, 265]}, {'text': 'MumbaiIndians', 'indices': [266, 280]}], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/xi0XoleJB7', 'expanded_url': 'https://techmorenow.com/post/mi-vs-rcb-dream11-team-prediction-ipl-2020-match-48-dream11-ipl-2020-match-prediction-today', 'display_url': 'techmorenow.com/post/mi-vs-rcb…', 'indices': [51, 74]}], 'media': [{'id': 1321419968840298498, 'id_str': '1321419968840298498', 'indices': [281, 304], 'media_url': 'http://pbs.twimg.com/media/ElagdeHVcAIpxH8.jpg', 'media_url_https': 'https://pbs.twimg.com/media/ElagdeHVcAIpxH8.jpg', 'url': 'https://t.co/amAsv1iUk6', 'display_url': 'pic.twitter.com/amAsv1iUk6', 'expanded_url': 'https://twitter.com/Dream1126329148/status/1321419976712974336/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'small': {'w': 680, 'h': 378, 'resize': 'fit'}, 'medium': {'w': 800, 'h': 445, 'resize': 'fit'}, 'large': {'w': 800, 'h': 445, 'resize': 'fit'}}}]}, 'extended_entities': {'media': [{'id': 1321419968840298498, 'id_str': '1321419968840298498', 'indices': [281, 304], 'media_url': 'http://pbs.twimg.com/media/ElagdeHVcAIpxH8.jpg', 'media_url_https': 'https://pbs.twimg.com/media/ElagdeHVcAIpxH8.jpg', 'url': 'https://t.co/amAsv1iUk6', 'display_url': 'pic.twitter.com/amAsv1iUk6', 'expanded_url': 'https://twitter.com/Dream1126329148/status/1321419976712974336/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'small': {'w': 680, 'h': 378, 'resize': 'fit'}, 'medium': {'w': 800, 'h': 445, 'resize': 'fit'}, 'large': {'w': 800, 'h': 445, 'resize': 'fit'}}}]}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 1306460760801828864, 'id_str': '1306460760801828864', 'name': 'Dream11Prediction', 'screen_name': 'Dream1126329148', 'location': '', 'description': '100% Winning Free Dream11 Prediction\\nEarned More than 1 Crore from Dream11 and other Fantasy leagues, Visit our Website for teams #Dream11ipl #dream11prediction', 'url': 'https://t.co/THLvE5rwDh', 'entities': {'url': {'urls': [{'url': 'https://t.co/THLvE5rwDh', 'expanded_url': 'https://www.techmorenow.com/', 'display_url': 'techmorenow.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 136, 'friends_count': 462, 'listed_count': 0, 'created_at': 'Thu Sep 17 05:12:04 +0000 2020', 'favourites_count': 86, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 422, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1306460760801828864/1601959416', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 1, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 10, 28, 11, 54, 7), id=1321419976712974336, id_str='1321419976712974336', full_text='MI vs RCB Dream11 Winning Team Prediction\\n\\nVisit : https://t.co/xi0XoleJB7\\n\\n#Dream11IPL #Dream11 #Dream11Team #dream11Prediction #Dream11IPL2020 #Dream11Tips #IPL2020 #IPLinUAE #IPL #IPLT20 #MI #RCB #MIvsRCB #MIvRCB #RCBvMI #RCBvsMI #ViratKohli #HITMAN #RohitSharma #MumbaiIndians https://t.co/amAsv1iUk6', truncated=False, display_text_range=[0, 280], entities={'hashtags': [{'text': 'Dream11IPL', 'indices': [76, 87]}, {'text': 'Dream11', 'indices': [88, 96]}, {'text': 'Dream11Team', 'indices': [97, 109]}, {'text': 'dream11Prediction', 'indices': [110, 128]}, {'text': 'Dream11IPL2020', 'indices': [129, 144]}, {'text': 'Dream11Tips', 'indices': [145, 157]}, {'text': 'IPL2020', 'indices': [158, 166]}, {'text': 'IPLinUAE', 'indices': [167, 176]}, {'text': 'IPL', 'indices': [177, 181]}, {'text': 'IPLT20', 'indices': [182, 189]}, {'text': 'MI', 'indices': [190, 193]}, {'text': 'RCB', 'indices': [194, 198]}, {'text': 'MIvsRCB', 'indices': [199, 207]}, {'text': 'MIvRCB', 'indices': [208, 215]}, {'text': 'RCBvMI', 'indices': [216, 223]}, {'text': 'RCBvsMI', 'indices': [224, 232]}, {'text': 'ViratKohli', 'indices': [233, 244]}, {'text': 'HITMAN', 'indices': [245, 252]}, {'text': 'RohitSharma', 'indices': [253, 265]}, {'text': 'MumbaiIndians', 'indices': [266, 280]}], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/xi0XoleJB7', 'expanded_url': 'https://techmorenow.com/post/mi-vs-rcb-dream11-team-prediction-ipl-2020-match-48-dream11-ipl-2020-match-prediction-today', 'display_url': 'techmorenow.com/post/mi-vs-rcb…', 'indices': [51, 74]}], 'media': [{'id': 1321419968840298498, 'id_str': '1321419968840298498', 'indices': [281, 304], 'media_url': 'http://pbs.twimg.com/media/ElagdeHVcAIpxH8.jpg', 'media_url_https': 'https://pbs.twimg.com/media/ElagdeHVcAIpxH8.jpg', 'url': 'https://t.co/amAsv1iUk6', 'display_url': 'pic.twitter.com/amAsv1iUk6', 'expanded_url': 'https://twitter.com/Dream1126329148/status/1321419976712974336/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'small': {'w': 680, 'h': 378, 'resize': 'fit'}, 'medium': {'w': 800, 'h': 445, 'resize': 'fit'}, 'large': {'w': 800, 'h': 445, 'resize': 'fit'}}}]}, extended_entities={'media': [{'id': 1321419968840298498, 'id_str': '1321419968840298498', 'indices': [281, 304], 'media_url': 'http://pbs.twimg.com/media/ElagdeHVcAIpxH8.jpg', 'media_url_https': 'https://pbs.twimg.com/media/ElagdeHVcAIpxH8.jpg', 'url': 'https://t.co/amAsv1iUk6', 'display_url': 'pic.twitter.com/amAsv1iUk6', 'expanded_url': 'https://twitter.com/Dream1126329148/status/1321419976712974336/photo/1', 'type': 'photo', 'sizes': {'thumb': {'w': 150, 'h': 150, 'resize': 'crop'}, 'small': {'w': 680, 'h': 378, 'resize': 'fit'}, 'medium': {'w': 800, 'h': 445, 'resize': 'fit'}, 'large': {'w': 800, 'h': 445, 'resize': 'fit'}}}]}, metadata={'iso_language_code': 'en', 'result_type': 'recent'}, source='Twitter Web App', source_url='https://mobile.twitter.com', in_reply_to_status_id=None, in_reply_to_status_id_str=None, in_reply_to_user_id=None, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, author=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 1306460760801828864, 'id_str': '1306460760801828864', 'name': 'Dream11Prediction', 'screen_name': 'Dream1126329148', 'location': '', 'description': '100% Winning Free Dream11 Prediction\\nEarned More than 1 Crore from Dream11 and other Fantasy leagues, Visit our Website for teams #Dream11ipl #dream11prediction', 'url': 'https://t.co/THLvE5rwDh', 'entities': {'url': {'urls': [{'url': 'https://t.co/THLvE5rwDh', 'expanded_url': 'https://www.techmorenow.com/', 'display_url': 'techmorenow.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 136, 'friends_count': 462, 'listed_count': 0, 'created_at': 'Thu Sep 17 05:12:04 +0000 2020', 'favourites_count': 86, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 422, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1306460760801828864/1601959416', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=1306460760801828864, id_str='1306460760801828864', name='Dream11Prediction', screen_name='Dream1126329148', location='', description='100% Winning Free Dream11 Prediction\\nEarned More than 1 Crore from Dream11 and other Fantasy leagues, Visit our Website for teams #Dream11ipl #dream11prediction', url='https://t.co/THLvE5rwDh', entities={'url': {'urls': [{'url': 'https://t.co/THLvE5rwDh', 'expanded_url': 'https://www.techmorenow.com/', 'display_url': 'techmorenow.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=136, friends_count=462, listed_count=0, created_at=datetime.datetime(2020, 9, 17, 5, 12, 4), favourites_count=86, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=422, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='F5F8FA', profile_background_image_url=None, profile_background_image_url_https=None, profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/1306460760801828864/1601959416', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=True, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), user=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 1306460760801828864, 'id_str': '1306460760801828864', 'name': 'Dream11Prediction', 'screen_name': 'Dream1126329148', 'location': '', 'description': '100% Winning Free Dream11 Prediction\\nEarned More than 1 Crore from Dream11 and other Fantasy leagues, Visit our Website for teams #Dream11ipl #dream11prediction', 'url': 'https://t.co/THLvE5rwDh', 'entities': {'url': {'urls': [{'url': 'https://t.co/THLvE5rwDh', 'expanded_url': 'https://www.techmorenow.com/', 'display_url': 'techmorenow.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 136, 'friends_count': 462, 'listed_count': 0, 'created_at': 'Thu Sep 17 05:12:04 +0000 2020', 'favourites_count': 86, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 422, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1306460760801828864/1601959416', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=1306460760801828864, id_str='1306460760801828864', name='Dream11Prediction', screen_name='Dream1126329148', location='', description='100% Winning Free Dream11 Prediction\\nEarned More than 1 Crore from Dream11 and other Fantasy leagues, Visit our Website for teams #Dream11ipl #dream11prediction', url='https://t.co/THLvE5rwDh', entities={'url': {'urls': [{'url': 'https://t.co/THLvE5rwDh', 'expanded_url': 'https://www.techmorenow.com/', 'display_url': 'techmorenow.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=136, friends_count=462, listed_count=0, created_at=datetime.datetime(2020, 9, 17, 5, 12, 4), favourites_count=86, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=422, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='F5F8FA', profile_background_image_url=None, profile_background_image_url_https=None, profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/1306460760801828864/1601959416', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=True, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=1, favorited=False, retweeted=False, possibly_sensitive=False, lang='en') \n",
      "\n",
      ".....................................\n",
      "\n",
      "Status(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'created_at': 'Wed Oct 28 11:47:03 +0000 2020', 'id': 1321418195551416320, 'id_str': '1321418195551416320', 'full_text': 'It’s #MIvsRCB today, last time it was #RCB who took the two points after winning a thrilling super over. \\nWho do you think will win today and seal their spot in the playoffs?\\n\\n#MI #RCB #PlayBold #MumbaiIndians #Dream11IPL #IPL #IPLinUAE #IPL2020', 'truncated': False, 'display_text_range': [0, 245], 'entities': {'hashtags': [{'text': 'MIvsRCB', 'indices': [5, 13]}, {'text': 'RCB', 'indices': [38, 42]}, {'text': 'MI', 'indices': [176, 179]}, {'text': 'RCB', 'indices': [180, 184]}, {'text': 'PlayBold', 'indices': [185, 194]}, {'text': 'MumbaiIndians', 'indices': [195, 209]}, {'text': 'Dream11IPL', 'indices': [210, 221]}, {'text': 'IPL', 'indices': [222, 226]}, {'text': 'IPLinUAE', 'indices': [227, 236]}, {'text': 'IPL2020', 'indices': [237, 245]}], 'symbols': [], 'user_mentions': [], 'urls': []}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 3692347394, 'id_str': '3692347394', 'name': 'Beyond the Panorama', 'screen_name': 'ReadBTP', 'location': 'India', 'description': 'Your daily dose of reading - short stories, poetry, and thoughts. Online Storytelling Magazine & Boutique Social Media Consultancy.', 'url': 'https://t.co/wDkan4nJ2r', 'entities': {'url': {'urls': [{'url': 'https://t.co/wDkan4nJ2r', 'expanded_url': 'http://www.beyondthepanorama.com', 'display_url': 'beyondthepanorama.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 65, 'friends_count': 117, 'listed_count': 3, 'created_at': 'Sat Sep 26 12:05:56 +0000 2015', 'favourites_count': 79, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 498, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1267107278366208000/-6KCuQJY_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1267107278366208000/-6KCuQJY_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/3692347394/1591033281', 'profile_link_color': '3B94D9', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 10, 28, 11, 47, 3), id=1321418195551416320, id_str='1321418195551416320', full_text='It’s #MIvsRCB today, last time it was #RCB who took the two points after winning a thrilling super over. \\nWho do you think will win today and seal their spot in the playoffs?\\n\\n#MI #RCB #PlayBold #MumbaiIndians #Dream11IPL #IPL #IPLinUAE #IPL2020', truncated=False, display_text_range=[0, 245], entities={'hashtags': [{'text': 'MIvsRCB', 'indices': [5, 13]}, {'text': 'RCB', 'indices': [38, 42]}, {'text': 'MI', 'indices': [176, 179]}, {'text': 'RCB', 'indices': [180, 184]}, {'text': 'PlayBold', 'indices': [185, 194]}, {'text': 'MumbaiIndians', 'indices': [195, 209]}, {'text': 'Dream11IPL', 'indices': [210, 221]}, {'text': 'IPL', 'indices': [222, 226]}, {'text': 'IPLinUAE', 'indices': [227, 236]}, {'text': 'IPL2020', 'indices': [237, 245]}], 'symbols': [], 'user_mentions': [], 'urls': []}, metadata={'iso_language_code': 'en', 'result_type': 'recent'}, source='Twitter for iPhone', source_url='http://twitter.com/download/iphone', in_reply_to_status_id=None, in_reply_to_status_id_str=None, in_reply_to_user_id=None, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, author=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 3692347394, 'id_str': '3692347394', 'name': 'Beyond the Panorama', 'screen_name': 'ReadBTP', 'location': 'India', 'description': 'Your daily dose of reading - short stories, poetry, and thoughts. Online Storytelling Magazine & Boutique Social Media Consultancy.', 'url': 'https://t.co/wDkan4nJ2r', 'entities': {'url': {'urls': [{'url': 'https://t.co/wDkan4nJ2r', 'expanded_url': 'http://www.beyondthepanorama.com', 'display_url': 'beyondthepanorama.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 65, 'friends_count': 117, 'listed_count': 3, 'created_at': 'Sat Sep 26 12:05:56 +0000 2015', 'favourites_count': 79, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 498, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1267107278366208000/-6KCuQJY_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1267107278366208000/-6KCuQJY_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/3692347394/1591033281', 'profile_link_color': '3B94D9', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=3692347394, id_str='3692347394', name='Beyond the Panorama', screen_name='ReadBTP', location='India', description='Your daily dose of reading - short stories, poetry, and thoughts. Online Storytelling Magazine & Boutique Social Media Consultancy.', url='https://t.co/wDkan4nJ2r', entities={'url': {'urls': [{'url': 'https://t.co/wDkan4nJ2r', 'expanded_url': 'http://www.beyondthepanorama.com', 'display_url': 'beyondthepanorama.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=65, friends_count=117, listed_count=3, created_at=datetime.datetime(2015, 9, 26, 12, 5, 56), favourites_count=79, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=498, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='000000', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1267107278366208000/-6KCuQJY_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1267107278366208000/-6KCuQJY_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/3692347394/1591033281', profile_link_color='3B94D9', profile_sidebar_border_color='000000', profile_sidebar_fill_color='000000', profile_text_color='000000', profile_use_background_image=False, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), user=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 3692347394, 'id_str': '3692347394', 'name': 'Beyond the Panorama', 'screen_name': 'ReadBTP', 'location': 'India', 'description': 'Your daily dose of reading - short stories, poetry, and thoughts. Online Storytelling Magazine & Boutique Social Media Consultancy.', 'url': 'https://t.co/wDkan4nJ2r', 'entities': {'url': {'urls': [{'url': 'https://t.co/wDkan4nJ2r', 'expanded_url': 'http://www.beyondthepanorama.com', 'display_url': 'beyondthepanorama.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 65, 'friends_count': 117, 'listed_count': 3, 'created_at': 'Sat Sep 26 12:05:56 +0000 2015', 'favourites_count': 79, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 498, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': '000000', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1267107278366208000/-6KCuQJY_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1267107278366208000/-6KCuQJY_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/3692347394/1591033281', 'profile_link_color': '3B94D9', 'profile_sidebar_border_color': '000000', 'profile_sidebar_fill_color': '000000', 'profile_text_color': '000000', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=3692347394, id_str='3692347394', name='Beyond the Panorama', screen_name='ReadBTP', location='India', description='Your daily dose of reading - short stories, poetry, and thoughts. Online Storytelling Magazine & Boutique Social Media Consultancy.', url='https://t.co/wDkan4nJ2r', entities={'url': {'urls': [{'url': 'https://t.co/wDkan4nJ2r', 'expanded_url': 'http://www.beyondthepanorama.com', 'display_url': 'beyondthepanorama.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=65, friends_count=117, listed_count=3, created_at=datetime.datetime(2015, 9, 26, 12, 5, 56), favourites_count=79, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=498, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='000000', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1267107278366208000/-6KCuQJY_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1267107278366208000/-6KCuQJY_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/3692347394/1591033281', profile_link_color='3B94D9', profile_sidebar_border_color='000000', profile_sidebar_fill_color='000000', profile_text_color='000000', profile_use_background_image=False, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=0, favorited=False, retweeted=False, lang='en') \n",
      "\n",
      ".....................................\n",
      "\n",
      "Status(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'created_at': 'Wed Oct 28 11:35:10 +0000 2020', 'id': 1321415205293674496, 'id_str': '1321415205293674496', 'full_text': '@KKRiders @chakaravarthy29 MI vs RCB Dream11 Winning Team Prediction\\n\\nVisit : https://t.co/xi0XoleJB7', 'truncated': False, 'display_text_range': [27, 101], 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'KKRiders', 'name': 'KolkataKnightRiders', 'id': 23592970, 'id_str': '23592970', 'indices': [0, 9]}, {'screen_name': 'chakaravarthy29', 'name': 'Varun Chakaravarthy', 'id': 1321103853899534337, 'id_str': '1321103853899534337', 'indices': [10, 26]}], 'urls': [{'url': 'https://t.co/xi0XoleJB7', 'expanded_url': 'https://techmorenow.com/post/mi-vs-rcb-dream11-team-prediction-ipl-2020-match-48-dream11-ipl-2020-match-prediction-today', 'display_url': 'techmorenow.com/post/mi-vs-rcb…', 'indices': [78, 101]}]}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>', 'in_reply_to_status_id': 1321413934105026561, 'in_reply_to_status_id_str': '1321413934105026561', 'in_reply_to_user_id': 23592970, 'in_reply_to_user_id_str': '23592970', 'in_reply_to_screen_name': 'KKRiders', 'user': {'id': 1306460760801828864, 'id_str': '1306460760801828864', 'name': 'Dream11Prediction', 'screen_name': 'Dream1126329148', 'location': '', 'description': '100% Winning Free Dream11 Prediction\\nEarned More than 1 Crore from Dream11 and other Fantasy leagues, Visit our Website for teams #Dream11ipl #dream11prediction', 'url': 'https://t.co/THLvE5rwDh', 'entities': {'url': {'urls': [{'url': 'https://t.co/THLvE5rwDh', 'expanded_url': 'https://www.techmorenow.com/', 'display_url': 'techmorenow.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 136, 'friends_count': 462, 'listed_count': 0, 'created_at': 'Thu Sep 17 05:12:04 +0000 2020', 'favourites_count': 86, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 422, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1306460760801828864/1601959416', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 10, 28, 11, 35, 10), id=1321415205293674496, id_str='1321415205293674496', full_text='@KKRiders @chakaravarthy29 MI vs RCB Dream11 Winning Team Prediction\\n\\nVisit : https://t.co/xi0XoleJB7', truncated=False, display_text_range=[27, 101], entities={'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'KKRiders', 'name': 'KolkataKnightRiders', 'id': 23592970, 'id_str': '23592970', 'indices': [0, 9]}, {'screen_name': 'chakaravarthy29', 'name': 'Varun Chakaravarthy', 'id': 1321103853899534337, 'id_str': '1321103853899534337', 'indices': [10, 26]}], 'urls': [{'url': 'https://t.co/xi0XoleJB7', 'expanded_url': 'https://techmorenow.com/post/mi-vs-rcb-dream11-team-prediction-ipl-2020-match-48-dream11-ipl-2020-match-prediction-today', 'display_url': 'techmorenow.com/post/mi-vs-rcb…', 'indices': [78, 101]}]}, metadata={'iso_language_code': 'en', 'result_type': 'recent'}, source='Twitter Web App', source_url='https://mobile.twitter.com', in_reply_to_status_id=1321413934105026561, in_reply_to_status_id_str='1321413934105026561', in_reply_to_user_id=23592970, in_reply_to_user_id_str='23592970', in_reply_to_screen_name='KKRiders', author=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 1306460760801828864, 'id_str': '1306460760801828864', 'name': 'Dream11Prediction', 'screen_name': 'Dream1126329148', 'location': '', 'description': '100% Winning Free Dream11 Prediction\\nEarned More than 1 Crore from Dream11 and other Fantasy leagues, Visit our Website for teams #Dream11ipl #dream11prediction', 'url': 'https://t.co/THLvE5rwDh', 'entities': {'url': {'urls': [{'url': 'https://t.co/THLvE5rwDh', 'expanded_url': 'https://www.techmorenow.com/', 'display_url': 'techmorenow.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 136, 'friends_count': 462, 'listed_count': 0, 'created_at': 'Thu Sep 17 05:12:04 +0000 2020', 'favourites_count': 86, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 422, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1306460760801828864/1601959416', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=1306460760801828864, id_str='1306460760801828864', name='Dream11Prediction', screen_name='Dream1126329148', location='', description='100% Winning Free Dream11 Prediction\\nEarned More than 1 Crore from Dream11 and other Fantasy leagues, Visit our Website for teams #Dream11ipl #dream11prediction', url='https://t.co/THLvE5rwDh', entities={'url': {'urls': [{'url': 'https://t.co/THLvE5rwDh', 'expanded_url': 'https://www.techmorenow.com/', 'display_url': 'techmorenow.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=136, friends_count=462, listed_count=0, created_at=datetime.datetime(2020, 9, 17, 5, 12, 4), favourites_count=86, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=422, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='F5F8FA', profile_background_image_url=None, profile_background_image_url_https=None, profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/1306460760801828864/1601959416', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=True, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), user=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 1306460760801828864, 'id_str': '1306460760801828864', 'name': 'Dream11Prediction', 'screen_name': 'Dream1126329148', 'location': '', 'description': '100% Winning Free Dream11 Prediction\\nEarned More than 1 Crore from Dream11 and other Fantasy leagues, Visit our Website for teams #Dream11ipl #dream11prediction', 'url': 'https://t.co/THLvE5rwDh', 'entities': {'url': {'urls': [{'url': 'https://t.co/THLvE5rwDh', 'expanded_url': 'https://www.techmorenow.com/', 'display_url': 'techmorenow.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 136, 'friends_count': 462, 'listed_count': 0, 'created_at': 'Thu Sep 17 05:12:04 +0000 2020', 'favourites_count': 86, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 422, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1306460760801828864/1601959416', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=1306460760801828864, id_str='1306460760801828864', name='Dream11Prediction', screen_name='Dream1126329148', location='', description='100% Winning Free Dream11 Prediction\\nEarned More than 1 Crore from Dream11 and other Fantasy leagues, Visit our Website for teams #Dream11ipl #dream11prediction', url='https://t.co/THLvE5rwDh', entities={'url': {'urls': [{'url': 'https://t.co/THLvE5rwDh', 'expanded_url': 'https://www.techmorenow.com/', 'display_url': 'techmorenow.com', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=136, friends_count=462, listed_count=0, created_at=datetime.datetime(2020, 9, 17, 5, 12, 4), favourites_count=86, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=422, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='F5F8FA', profile_background_image_url=None, profile_background_image_url_https=None, profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1306461080298823680/GYGBV0Hl_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/1306460760801828864/1601959416', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=True, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=0, favorited=False, retweeted=False, possibly_sensitive=False, lang='en') \n",
      "\n",
      ".....................................\n",
      "\n",
      "Status(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'created_at': 'Wed Oct 28 11:20:59 +0000 2020', 'id': 1321411635425071105, 'id_str': '1321411635425071105', 'full_text': '@mipaltan @IPL_POLL @KieronPollard55 Today match #MIvsRCB is just kids play\\n\\nLion @RCBTweets vs mouse @mipaltan ...\\n\\n if @RCBTweets Decides to Bat First after Winning Toss #Mi will try to defeat them..🤔\\n\\nBut If #PlayBold Decides to ball First Forgot #Mi to win..Now all up to what RCB Decides after winning toss🔥...', 'truncated': False, 'display_text_range': [37, 315], 'entities': {'hashtags': [{'text': 'MIvsRCB', 'indices': [49, 57]}, {'text': 'Mi', 'indices': [172, 175]}, {'text': 'PlayBold', 'indices': [211, 220]}, {'text': 'Mi', 'indices': [250, 253]}], 'symbols': [], 'user_mentions': [{'screen_name': 'mipaltan', 'name': 'Mumbai Indians', 'id': 106345557, 'id_str': '106345557', 'indices': [0, 9]}, {'screen_name': 'IPL_POLL', 'name': '⚔️ IPL POLL ⚔️ 🔻🔼(MI⚔️RCB)', 'id': 1298931734768021504, 'id_str': '1298931734768021504', 'indices': [10, 19]}, {'screen_name': 'KieronPollard55', 'name': 'Kieron Pollard', 'id': 281947148, 'id_str': '281947148', 'indices': [20, 36]}, {'screen_name': 'RCBTweets', 'name': 'Royal Challengers Bangalore', 'id': 70931004, 'id_str': '70931004', 'indices': [82, 92]}, {'screen_name': 'mipaltan', 'name': 'Mumbai Indians', 'id': 106345557, 'id_str': '106345557', 'indices': [102, 111]}, {'screen_name': 'RCBTweets', 'name': 'Royal Challengers Bangalore', 'id': 70931004, 'id_str': '70931004', 'indices': [121, 131]}], 'urls': []}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>', 'in_reply_to_status_id': 1321391261912158210, 'in_reply_to_status_id_str': '1321391261912158210', 'in_reply_to_user_id': 106345557, 'in_reply_to_user_id_str': '106345557', 'in_reply_to_screen_name': 'mipaltan', 'user': {'id': 1263648459212705794, 'id_str': '1263648459212705794', 'name': '$ensational $oumya ❤️', 'screen_name': 'Im_soumyaa', 'location': 'Mumbai, India', 'description': '#Chartered_Accountant ❤️ | Guitarist 🎸 | Love ✈️ 2 Solo Traveling | @Klrahul11 ❤️ | @Chemistry❤️ |Bharatiyo_Janata_party 👑 |#Satyamev_Jayate 🇮🇳', 'url': 'https://t.co/9D2aN87z3W', 'entities': {'url': {'urls': [{'url': 'https://t.co/9D2aN87z3W', 'expanded_url': 'https://instagram.com/neel_bhattacharya?igshid=j0pzwjwjqykh', 'display_url': 'instagram.com/neel_bhattacha…', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 183, 'friends_count': 269, 'listed_count': 0, 'created_at': 'Fri May 22 01:51:03 +0000 2020', 'favourites_count': 3168, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 2090, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1320082345529995264/lXCd809u_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1320082345529995264/lXCd809u_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1263648459212705794/1603284949', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 2, 'favorited': False, 'retweeted': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 10, 28, 11, 20, 59), id=1321411635425071105, id_str='1321411635425071105', full_text='@mipaltan @IPL_POLL @KieronPollard55 Today match #MIvsRCB is just kids play\\n\\nLion @RCBTweets vs mouse @mipaltan ...\\n\\n if @RCBTweets Decides to Bat First after Winning Toss #Mi will try to defeat them..🤔\\n\\nBut If #PlayBold Decides to ball First Forgot #Mi to win..Now all up to what RCB Decides after winning toss🔥...', truncated=False, display_text_range=[37, 315], entities={'hashtags': [{'text': 'MIvsRCB', 'indices': [49, 57]}, {'text': 'Mi', 'indices': [172, 175]}, {'text': 'PlayBold', 'indices': [211, 220]}, {'text': 'Mi', 'indices': [250, 253]}], 'symbols': [], 'user_mentions': [{'screen_name': 'mipaltan', 'name': 'Mumbai Indians', 'id': 106345557, 'id_str': '106345557', 'indices': [0, 9]}, {'screen_name': 'IPL_POLL', 'name': '⚔️ IPL POLL ⚔️ 🔻🔼(MI⚔️RCB)', 'id': 1298931734768021504, 'id_str': '1298931734768021504', 'indices': [10, 19]}, {'screen_name': 'KieronPollard55', 'name': 'Kieron Pollard', 'id': 281947148, 'id_str': '281947148', 'indices': [20, 36]}, {'screen_name': 'RCBTweets', 'name': 'Royal Challengers Bangalore', 'id': 70931004, 'id_str': '70931004', 'indices': [82, 92]}, {'screen_name': 'mipaltan', 'name': 'Mumbai Indians', 'id': 106345557, 'id_str': '106345557', 'indices': [102, 111]}, {'screen_name': 'RCBTweets', 'name': 'Royal Challengers Bangalore', 'id': 70931004, 'id_str': '70931004', 'indices': [121, 131]}], 'urls': []}, metadata={'iso_language_code': 'en', 'result_type': 'recent'}, source='Twitter for Android', source_url='http://twitter.com/download/android', in_reply_to_status_id=1321391261912158210, in_reply_to_status_id_str='1321391261912158210', in_reply_to_user_id=106345557, in_reply_to_user_id_str='106345557', in_reply_to_screen_name='mipaltan', author=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 1263648459212705794, 'id_str': '1263648459212705794', 'name': '$ensational $oumya ❤️', 'screen_name': 'Im_soumyaa', 'location': 'Mumbai, India', 'description': '#Chartered_Accountant ❤️ | Guitarist 🎸 | Love ✈️ 2 Solo Traveling | @Klrahul11 ❤️ | @Chemistry❤️ |Bharatiyo_Janata_party 👑 |#Satyamev_Jayate 🇮🇳', 'url': 'https://t.co/9D2aN87z3W', 'entities': {'url': {'urls': [{'url': 'https://t.co/9D2aN87z3W', 'expanded_url': 'https://instagram.com/neel_bhattacharya?igshid=j0pzwjwjqykh', 'display_url': 'instagram.com/neel_bhattacha…', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 183, 'friends_count': 269, 'listed_count': 0, 'created_at': 'Fri May 22 01:51:03 +0000 2020', 'favourites_count': 3168, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 2090, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1320082345529995264/lXCd809u_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1320082345529995264/lXCd809u_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1263648459212705794/1603284949', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=1263648459212705794, id_str='1263648459212705794', name='$ensational $oumya ❤️', screen_name='Im_soumyaa', location='Mumbai, India', description='#Chartered_Accountant ❤️ | Guitarist 🎸 | Love ✈️ 2 Solo Traveling | @Klrahul11 ❤️ | @Chemistry❤️ |Bharatiyo_Janata_party 👑 |#Satyamev_Jayate 🇮🇳', url='https://t.co/9D2aN87z3W', entities={'url': {'urls': [{'url': 'https://t.co/9D2aN87z3W', 'expanded_url': 'https://instagram.com/neel_bhattacharya?igshid=j0pzwjwjqykh', 'display_url': 'instagram.com/neel_bhattacha…', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=183, friends_count=269, listed_count=0, created_at=datetime.datetime(2020, 5, 22, 1, 51, 3), favourites_count=3168, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=2090, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='F5F8FA', profile_background_image_url=None, profile_background_image_url_https=None, profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1320082345529995264/lXCd809u_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1320082345529995264/lXCd809u_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/1263648459212705794/1603284949', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=True, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), user=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 1263648459212705794, 'id_str': '1263648459212705794', 'name': '$ensational $oumya ❤️', 'screen_name': 'Im_soumyaa', 'location': 'Mumbai, India', 'description': '#Chartered_Accountant ❤️ | Guitarist 🎸 | Love ✈️ 2 Solo Traveling | @Klrahul11 ❤️ | @Chemistry❤️ |Bharatiyo_Janata_party 👑 |#Satyamev_Jayate 🇮🇳', 'url': 'https://t.co/9D2aN87z3W', 'entities': {'url': {'urls': [{'url': 'https://t.co/9D2aN87z3W', 'expanded_url': 'https://instagram.com/neel_bhattacharya?igshid=j0pzwjwjqykh', 'display_url': 'instagram.com/neel_bhattacha…', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 183, 'friends_count': 269, 'listed_count': 0, 'created_at': 'Fri May 22 01:51:03 +0000 2020', 'favourites_count': 3168, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 2090, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1320082345529995264/lXCd809u_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1320082345529995264/lXCd809u_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/1263648459212705794/1603284949', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=1263648459212705794, id_str='1263648459212705794', name='$ensational $oumya ❤️', screen_name='Im_soumyaa', location='Mumbai, India', description='#Chartered_Accountant ❤️ | Guitarist 🎸 | Love ✈️ 2 Solo Traveling | @Klrahul11 ❤️ | @Chemistry❤️ |Bharatiyo_Janata_party 👑 |#Satyamev_Jayate 🇮🇳', url='https://t.co/9D2aN87z3W', entities={'url': {'urls': [{'url': 'https://t.co/9D2aN87z3W', 'expanded_url': 'https://instagram.com/neel_bhattacharya?igshid=j0pzwjwjqykh', 'display_url': 'instagram.com/neel_bhattacha…', 'indices': [0, 23]}]}, 'description': {'urls': []}}, protected=False, followers_count=183, friends_count=269, listed_count=0, created_at=datetime.datetime(2020, 5, 22, 1, 51, 3), favourites_count=3168, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=2090, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='F5F8FA', profile_background_image_url=None, profile_background_image_url_https=None, profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1320082345529995264/lXCd809u_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1320082345529995264/lXCd809u_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/1263648459212705794/1603284949', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=True, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=2, favorited=False, retweeted=False, lang='en') \n",
      "\n",
      ".....................................\n",
      "\n",
      "Status(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'created_at': 'Wed Oct 28 11:05:43 +0000 2020', 'id': 1321407792821907456, 'id_str': '1321407792821907456', 'full_text': 'RCB winning IPL https://t.co/R52vMRTi5r', 'truncated': False, 'display_text_range': [0, 15], 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/R52vMRTi5r', 'expanded_url': 'https://twitter.com/ESPNcricinfo/status/1321399258096918528', 'display_url': 'twitter.com/ESPNcricinfo/s…', 'indices': [16, 39]}]}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"http://twitter.com/download/android\" rel=\"nofollow\">Twitter for Android</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 704532714230140930, 'id_str': '704532714230140930', 'name': 'Ⓢⓤⓝⓝⓨ', 'screen_name': 'Sunny____123', 'location': '', 'description': 'Bio cannot be blank', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 1427, 'friends_count': 1538, 'listed_count': 35, 'created_at': 'Tue Mar 01 05:04:23 +0000 2016', 'favourites_count': 63670, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 52913, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1303783821242847232/oDEjK3sJ_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1303783821242847232/oDEjK3sJ_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/704532714230140930/1603301428', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': True, 'quoted_status_id': 1321399258096918528, 'quoted_status_id_str': '1321399258096918528', 'quoted_status': {'created_at': 'Wed Oct 28 10:31:48 +0000 2020', 'id': 1321399258096918528, 'id_str': '1321399258096918528', 'full_text': 'What has surprised you the most about #IPL2020?', 'truncated': False, 'display_text_range': [0, 47], 'entities': {'hashtags': [{'text': 'IPL2020', 'indices': [38, 46]}], 'symbols': [], 'user_mentions': [], 'urls': []}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 16542390, 'id_str': '16542390', 'name': 'ESPNcricinfo', 'screen_name': 'ESPNcricinfo', 'location': 'At the cricket, mainly', 'description': 'Scores and lot more!\\n\\nLog on to https://t.co/suKnazEYwH', 'url': 'http://t.co/IGblfozhqG', 'entities': {'url': {'urls': [{'url': 'http://t.co/IGblfozhqG', 'expanded_url': 'http://www.espncricinfo.com/', 'display_url': 'espncricinfo.com', 'indices': [0, 22]}]}, 'description': {'urls': [{'url': 'https://t.co/suKnazEYwH', 'expanded_url': 'http://www.espncricinfo.com', 'display_url': 'espncricinfo.com', 'indices': [32, 55]}]}}, 'protected': False, 'followers_count': 5913041, 'friends_count': 200, 'listed_count': 5631, 'created_at': 'Wed Oct 01 10:36:44 +0000 2008', 'favourites_count': 244, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': True, 'statuses_count': 151696, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'E0E0E0', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme2/bg.gif', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme2/bg.gif', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/16542390/1600483638', 'profile_link_color': '1F98C7', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'DAECF4', 'profile_text_color': '663B12', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 27, 'favorite_count': 1543, 'favorited': False, 'retweeted': False, 'lang': 'en'}, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 10, 28, 11, 5, 43), id=1321407792821907456, id_str='1321407792821907456', full_text='RCB winning IPL https://t.co/R52vMRTi5r', truncated=False, display_text_range=[0, 15], entities={'hashtags': [], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/R52vMRTi5r', 'expanded_url': 'https://twitter.com/ESPNcricinfo/status/1321399258096918528', 'display_url': 'twitter.com/ESPNcricinfo/s…', 'indices': [16, 39]}]}, metadata={'iso_language_code': 'en', 'result_type': 'recent'}, source='Twitter for Android', source_url='http://twitter.com/download/android', in_reply_to_status_id=None, in_reply_to_status_id_str=None, in_reply_to_user_id=None, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, author=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 704532714230140930, 'id_str': '704532714230140930', 'name': 'Ⓢⓤⓝⓝⓨ', 'screen_name': 'Sunny____123', 'location': '', 'description': 'Bio cannot be blank', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 1427, 'friends_count': 1538, 'listed_count': 35, 'created_at': 'Tue Mar 01 05:04:23 +0000 2016', 'favourites_count': 63670, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 52913, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1303783821242847232/oDEjK3sJ_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1303783821242847232/oDEjK3sJ_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/704532714230140930/1603301428', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=704532714230140930, id_str='704532714230140930', name='Ⓢⓤⓝⓝⓨ', screen_name='Sunny____123', location='', description='Bio cannot be blank', url=None, entities={'description': {'urls': []}}, protected=False, followers_count=1427, friends_count=1538, listed_count=35, created_at=datetime.datetime(2016, 3, 1, 5, 4, 23), favourites_count=63670, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=52913, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='F5F8FA', profile_background_image_url=None, profile_background_image_url_https=None, profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1303783821242847232/oDEjK3sJ_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1303783821242847232/oDEjK3sJ_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/704532714230140930/1603301428', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=False, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), user=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 704532714230140930, 'id_str': '704532714230140930', 'name': 'Ⓢⓤⓝⓝⓨ', 'screen_name': 'Sunny____123', 'location': '', 'description': 'Bio cannot be blank', 'url': None, 'entities': {'description': {'urls': []}}, 'protected': False, 'followers_count': 1427, 'friends_count': 1538, 'listed_count': 35, 'created_at': 'Tue Mar 01 05:04:23 +0000 2016', 'favourites_count': 63670, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 52913, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1303783821242847232/oDEjK3sJ_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1303783821242847232/oDEjK3sJ_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/704532714230140930/1603301428', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=704532714230140930, id_str='704532714230140930', name='Ⓢⓤⓝⓝⓨ', screen_name='Sunny____123', location='', description='Bio cannot be blank', url=None, entities={'description': {'urls': []}}, protected=False, followers_count=1427, friends_count=1538, listed_count=35, created_at=datetime.datetime(2016, 3, 1, 5, 4, 23), favourites_count=63670, utc_offset=None, time_zone=None, geo_enabled=False, verified=False, statuses_count=52913, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='F5F8FA', profile_background_image_url=None, profile_background_image_url_https=None, profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/1303783821242847232/oDEjK3sJ_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1303783821242847232/oDEjK3sJ_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/704532714230140930/1603301428', profile_link_color='1DA1F2', profile_sidebar_border_color='C0DEED', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=False, default_profile=True, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), geo=None, coordinates=None, place=None, contributors=None, is_quote_status=True, quoted_status_id=1321399258096918528, quoted_status_id_str='1321399258096918528', quoted_status=Status(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'created_at': 'Wed Oct 28 10:31:48 +0000 2020', 'id': 1321399258096918528, 'id_str': '1321399258096918528', 'full_text': 'What has surprised you the most about #IPL2020?', 'truncated': False, 'display_text_range': [0, 47], 'entities': {'hashtags': [{'text': 'IPL2020', 'indices': [38, 46]}], 'symbols': [], 'user_mentions': [], 'urls': []}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 16542390, 'id_str': '16542390', 'name': 'ESPNcricinfo', 'screen_name': 'ESPNcricinfo', 'location': 'At the cricket, mainly', 'description': 'Scores and lot more!\\n\\nLog on to https://t.co/suKnazEYwH', 'url': 'http://t.co/IGblfozhqG', 'entities': {'url': {'urls': [{'url': 'http://t.co/IGblfozhqG', 'expanded_url': 'http://www.espncricinfo.com/', 'display_url': 'espncricinfo.com', 'indices': [0, 22]}]}, 'description': {'urls': [{'url': 'https://t.co/suKnazEYwH', 'expanded_url': 'http://www.espncricinfo.com', 'display_url': 'espncricinfo.com', 'indices': [32, 55]}]}}, 'protected': False, 'followers_count': 5913041, 'friends_count': 200, 'listed_count': 5631, 'created_at': 'Wed Oct 01 10:36:44 +0000 2008', 'favourites_count': 244, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': True, 'statuses_count': 151696, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'E0E0E0', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme2/bg.gif', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme2/bg.gif', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/16542390/1600483638', 'profile_link_color': '1F98C7', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'DAECF4', 'profile_text_color': '663B12', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 27, 'favorite_count': 1543, 'favorited': False, 'retweeted': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 10, 28, 10, 31, 48), id=1321399258096918528, id_str='1321399258096918528', full_text='What has surprised you the most about #IPL2020?', truncated=False, display_text_range=[0, 47], entities={'hashtags': [{'text': 'IPL2020', 'indices': [38, 46]}], 'symbols': [], 'user_mentions': [], 'urls': []}, metadata={'iso_language_code': 'en', 'result_type': 'recent'}, source='TweetDeck', source_url='https://about.twitter.com/products/tweetdeck', in_reply_to_status_id=None, in_reply_to_status_id_str=None, in_reply_to_user_id=None, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, author=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 16542390, 'id_str': '16542390', 'name': 'ESPNcricinfo', 'screen_name': 'ESPNcricinfo', 'location': 'At the cricket, mainly', 'description': 'Scores and lot more!\\n\\nLog on to https://t.co/suKnazEYwH', 'url': 'http://t.co/IGblfozhqG', 'entities': {'url': {'urls': [{'url': 'http://t.co/IGblfozhqG', 'expanded_url': 'http://www.espncricinfo.com/', 'display_url': 'espncricinfo.com', 'indices': [0, 22]}]}, 'description': {'urls': [{'url': 'https://t.co/suKnazEYwH', 'expanded_url': 'http://www.espncricinfo.com', 'display_url': 'espncricinfo.com', 'indices': [32, 55]}]}}, 'protected': False, 'followers_count': 5913041, 'friends_count': 200, 'listed_count': 5631, 'created_at': 'Wed Oct 01 10:36:44 +0000 2008', 'favourites_count': 244, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': True, 'statuses_count': 151696, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'E0E0E0', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme2/bg.gif', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme2/bg.gif', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/16542390/1600483638', 'profile_link_color': '1F98C7', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'DAECF4', 'profile_text_color': '663B12', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=16542390, id_str='16542390', name='ESPNcricinfo', screen_name='ESPNcricinfo', location='At the cricket, mainly', description='Scores and lot more!\\n\\nLog on to https://t.co/suKnazEYwH', url='http://t.co/IGblfozhqG', entities={'url': {'urls': [{'url': 'http://t.co/IGblfozhqG', 'expanded_url': 'http://www.espncricinfo.com/', 'display_url': 'espncricinfo.com', 'indices': [0, 22]}]}, 'description': {'urls': [{'url': 'https://t.co/suKnazEYwH', 'expanded_url': 'http://www.espncricinfo.com', 'display_url': 'espncricinfo.com', 'indices': [32, 55]}]}}, protected=False, followers_count=5913041, friends_count=200, listed_count=5631, created_at=datetime.datetime(2008, 10, 1, 10, 36, 44), favourites_count=244, utc_offset=None, time_zone=None, geo_enabled=False, verified=True, statuses_count=151696, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='E0E0E0', profile_background_image_url='http://abs.twimg.com/images/themes/theme2/bg.gif', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme2/bg.gif', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/16542390/1600483638', profile_link_color='1F98C7', profile_sidebar_border_color='FFFFFF', profile_sidebar_fill_color='DAECF4', profile_text_color='663B12', profile_use_background_image=True, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), user=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 16542390, 'id_str': '16542390', 'name': 'ESPNcricinfo', 'screen_name': 'ESPNcricinfo', 'location': 'At the cricket, mainly', 'description': 'Scores and lot more!\\n\\nLog on to https://t.co/suKnazEYwH', 'url': 'http://t.co/IGblfozhqG', 'entities': {'url': {'urls': [{'url': 'http://t.co/IGblfozhqG', 'expanded_url': 'http://www.espncricinfo.com/', 'display_url': 'espncricinfo.com', 'indices': [0, 22]}]}, 'description': {'urls': [{'url': 'https://t.co/suKnazEYwH', 'expanded_url': 'http://www.espncricinfo.com', 'display_url': 'espncricinfo.com', 'indices': [32, 55]}]}}, 'protected': False, 'followers_count': 5913041, 'friends_count': 200, 'listed_count': 5631, 'created_at': 'Wed Oct 01 10:36:44 +0000 2008', 'favourites_count': 244, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': True, 'statuses_count': 151696, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'E0E0E0', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme2/bg.gif', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme2/bg.gif', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/16542390/1600483638', 'profile_link_color': '1F98C7', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'DAECF4', 'profile_text_color': '663B12', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=16542390, id_str='16542390', name='ESPNcricinfo', screen_name='ESPNcricinfo', location='At the cricket, mainly', description='Scores and lot more!\\n\\nLog on to https://t.co/suKnazEYwH', url='http://t.co/IGblfozhqG', entities={'url': {'urls': [{'url': 'http://t.co/IGblfozhqG', 'expanded_url': 'http://www.espncricinfo.com/', 'display_url': 'espncricinfo.com', 'indices': [0, 22]}]}, 'description': {'urls': [{'url': 'https://t.co/suKnazEYwH', 'expanded_url': 'http://www.espncricinfo.com', 'display_url': 'espncricinfo.com', 'indices': [32, 55]}]}}, protected=False, followers_count=5913041, friends_count=200, listed_count=5631, created_at=datetime.datetime(2008, 10, 1, 10, 36, 44), favourites_count=244, utc_offset=None, time_zone=None, geo_enabled=False, verified=True, statuses_count=151696, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='E0E0E0', profile_background_image_url='http://abs.twimg.com/images/themes/theme2/bg.gif', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme2/bg.gif', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/888015358958940165/SmaHw6Rj_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/16542390/1600483638', profile_link_color='1F98C7', profile_sidebar_border_color='FFFFFF', profile_sidebar_fill_color='DAECF4', profile_text_color='663B12', profile_use_background_image=True, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=27, favorite_count=1543, favorited=False, retweeted=False, lang='en'), retweet_count=0, favorite_count=0, favorited=False, retweeted=False, possibly_sensitive=False, lang='en') \n",
      "\n",
      ".....................................\n",
      "\n",
      "Status(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'created_at': 'Wed Oct 28 11:03:15 +0000 2020', 'id': 1321407172501143553, 'id_str': '1321407172501143553', 'full_text': '#IPL 2020 #MIvRCB | Mumbai Indians, Royal Challengers Bangalore lost their previous games. Will they return to winning ways tonight?\\n\\nFollow live updates:\\n\\nhttps://t.co/F0lsC13kwf', 'truncated': False, 'display_text_range': [0, 179], 'entities': {'hashtags': [{'text': 'IPL', 'indices': [0, 4]}, {'text': 'MIvRCB', 'indices': [10, 17]}], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/F0lsC13kwf', 'expanded_url': 'https://www.hindustantimes.com/cricket/ipl-2020-live-cricket-score-mumbai-indians-vs-royal-challengers-bangalore-latest-updates-mi-vs-rcb-indian-premier-league-48-match-today-live-updates/story-6cgPmfB2pVh460b5gW8HrI.html', 'display_url': 'hindustantimes.com/cricket/ipl-20…', 'indices': [156, 179]}]}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 2532884354, 'id_str': '2532884354', 'name': 'HT Sports', 'screen_name': 'HTSportsNews', 'location': 'India', 'description': \"India's premier destination for cricket, football, tennis and other sports from all over the world.\", 'url': 'http://t.co/4q7tpTsmJ2', 'entities': {'url': {'urls': [{'url': 'http://t.co/4q7tpTsmJ2', 'expanded_url': 'http://hindustantimes.com', 'display_url': 'hindustantimes.com', 'indices': [0, 22]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 101336, 'friends_count': 375, 'listed_count': 346, 'created_at': 'Thu May 29 15:42:59 +0000 2014', 'favourites_count': 339, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': True, 'statuses_count': 111184, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1299777577742073857/TzFpLDLX_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1299777577742073857/TzFpLDLX_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2532884354/1599448059', 'profile_link_color': '0084B4', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 1, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 10, 28, 11, 3, 15), id=1321407172501143553, id_str='1321407172501143553', full_text='#IPL 2020 #MIvRCB | Mumbai Indians, Royal Challengers Bangalore lost their previous games. Will they return to winning ways tonight?\\n\\nFollow live updates:\\n\\nhttps://t.co/F0lsC13kwf', truncated=False, display_text_range=[0, 179], entities={'hashtags': [{'text': 'IPL', 'indices': [0, 4]}, {'text': 'MIvRCB', 'indices': [10, 17]}], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/F0lsC13kwf', 'expanded_url': 'https://www.hindustantimes.com/cricket/ipl-2020-live-cricket-score-mumbai-indians-vs-royal-challengers-bangalore-latest-updates-mi-vs-rcb-indian-premier-league-48-match-today-live-updates/story-6cgPmfB2pVh460b5gW8HrI.html', 'display_url': 'hindustantimes.com/cricket/ipl-20…', 'indices': [156, 179]}]}, metadata={'iso_language_code': 'en', 'result_type': 'recent'}, source='TweetDeck', source_url='https://about.twitter.com/products/tweetdeck', in_reply_to_status_id=None, in_reply_to_status_id_str=None, in_reply_to_user_id=None, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, author=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 2532884354, 'id_str': '2532884354', 'name': 'HT Sports', 'screen_name': 'HTSportsNews', 'location': 'India', 'description': \"India's premier destination for cricket, football, tennis and other sports from all over the world.\", 'url': 'http://t.co/4q7tpTsmJ2', 'entities': {'url': {'urls': [{'url': 'http://t.co/4q7tpTsmJ2', 'expanded_url': 'http://hindustantimes.com', 'display_url': 'hindustantimes.com', 'indices': [0, 22]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 101336, 'friends_count': 375, 'listed_count': 346, 'created_at': 'Thu May 29 15:42:59 +0000 2014', 'favourites_count': 339, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': True, 'statuses_count': 111184, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1299777577742073857/TzFpLDLX_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1299777577742073857/TzFpLDLX_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2532884354/1599448059', 'profile_link_color': '0084B4', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=2532884354, id_str='2532884354', name='HT Sports', screen_name='HTSportsNews', location='India', description=\"India's premier destination for cricket, football, tennis and other sports from all over the world.\", url='http://t.co/4q7tpTsmJ2', entities={'url': {'urls': [{'url': 'http://t.co/4q7tpTsmJ2', 'expanded_url': 'http://hindustantimes.com', 'display_url': 'hindustantimes.com', 'indices': [0, 22]}]}, 'description': {'urls': []}}, protected=False, followers_count=101336, friends_count=375, listed_count=346, created_at=datetime.datetime(2014, 5, 29, 15, 42, 59), favourites_count=339, utc_offset=None, time_zone=None, geo_enabled=False, verified=True, statuses_count=111184, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='C0DEED', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=True, profile_image_url='http://pbs.twimg.com/profile_images/1299777577742073857/TzFpLDLX_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1299777577742073857/TzFpLDLX_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/2532884354/1599448059', profile_link_color='0084B4', profile_sidebar_border_color='FFFFFF', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=False, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), user=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 2532884354, 'id_str': '2532884354', 'name': 'HT Sports', 'screen_name': 'HTSportsNews', 'location': 'India', 'description': \"India's premier destination for cricket, football, tennis and other sports from all over the world.\", 'url': 'http://t.co/4q7tpTsmJ2', 'entities': {'url': {'urls': [{'url': 'http://t.co/4q7tpTsmJ2', 'expanded_url': 'http://hindustantimes.com', 'display_url': 'hindustantimes.com', 'indices': [0, 22]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 101336, 'friends_count': 375, 'listed_count': 346, 'created_at': 'Thu May 29 15:42:59 +0000 2014', 'favourites_count': 339, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': True, 'statuses_count': 111184, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': True, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1299777577742073857/TzFpLDLX_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1299777577742073857/TzFpLDLX_normal.jpg', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/2532884354/1599448059', 'profile_link_color': '0084B4', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': False, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=2532884354, id_str='2532884354', name='HT Sports', screen_name='HTSportsNews', location='India', description=\"India's premier destination for cricket, football, tennis and other sports from all over the world.\", url='http://t.co/4q7tpTsmJ2', entities={'url': {'urls': [{'url': 'http://t.co/4q7tpTsmJ2', 'expanded_url': 'http://hindustantimes.com', 'display_url': 'hindustantimes.com', 'indices': [0, 22]}]}, 'description': {'urls': []}}, protected=False, followers_count=101336, friends_count=375, listed_count=346, created_at=datetime.datetime(2014, 5, 29, 15, 42, 59), favourites_count=339, utc_offset=None, time_zone=None, geo_enabled=False, verified=True, statuses_count=111184, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='C0DEED', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=True, profile_image_url='http://pbs.twimg.com/profile_images/1299777577742073857/TzFpLDLX_normal.jpg', profile_image_url_https='https://pbs.twimg.com/profile_images/1299777577742073857/TzFpLDLX_normal.jpg', profile_banner_url='https://pbs.twimg.com/profile_banners/2532884354/1599448059', profile_link_color='0084B4', profile_sidebar_border_color='FFFFFF', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=False, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=1, favorited=False, retweeted=False, possibly_sensitive=False, lang='en') \n",
      "\n",
      ".....................................\n",
      "\n",
      "Status(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'created_at': 'Wed Oct 28 10:47:15 +0000 2020', 'id': 1321403147340845056, 'id_str': '1321403147340845056', 'full_text': \"Wriddhiman Saha had picked up the niggle during his match-winning innings of 87 off 45 balls against #DelhiCapitals on Tuesday and didn't keep wickets with substitute Shreevats Goswami replacing him. #IPL2020 \\n\\nhttps://t.co/kxn1wH5BfB\", 'truncated': False, 'display_text_range': [0, 234], 'entities': {'hashtags': [{'text': 'DelhiCapitals', 'indices': [101, 115]}, {'text': 'IPL2020', 'indices': [200, 208]}], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/kxn1wH5BfB', 'expanded_url': 'https://www.firstpost.com/firstcricket/sports-news/ipl-2020-wriddhiman-sahas-groin-injury-not-serious-but-srh-likely-to-wait-and-watch-ahead-of-rcb-game-8960001.html', 'display_url': 'firstpost.com/firstcricket/s…', 'indices': [211, 234]}]}, 'metadata': {'iso_language_code': 'en', 'result_type': 'recent'}, 'source': '<a href=\"https://about.twitter.com/products/tweetdeck\" rel=\"nofollow\">TweetDeck</a>', 'in_reply_to_status_id': None, 'in_reply_to_status_id_str': None, 'in_reply_to_user_id': None, 'in_reply_to_user_id_str': None, 'in_reply_to_screen_name': None, 'user': {'id': 335891957, 'id_str': '335891957', 'name': 'Firstpost Sports', 'screen_name': 'FirstpostSports', 'location': 'India', 'description': 'Bringing you live updates, breaking news, opinions and photos from the world of sport.', 'url': 'http://t.co/XSaFXN4DBr', 'entities': {'url': {'urls': [{'url': 'http://t.co/XSaFXN4DBr', 'expanded_url': 'http://www.firstpost.com/category/sports', 'display_url': 'firstpost.com/category/sports', 'indices': [0, 22]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 441638, 'friends_count': 873, 'listed_count': 550, 'created_at': 'Fri Jul 15 12:15:40 +0000 2011', 'favourites_count': 6, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': True, 'statuses_count': 207984, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/2503138588/lc89nnbhz3tvpkztrxhe_normal.png', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/2503138588/lc89nnbhz3tvpkztrxhe_normal.png', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/335891957/1531981823', 'profile_link_color': '0084B4', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 5, 'favorited': False, 'retweeted': False, 'possibly_sensitive': False, 'lang': 'en'}, created_at=datetime.datetime(2020, 10, 28, 10, 47, 15), id=1321403147340845056, id_str='1321403147340845056', full_text=\"Wriddhiman Saha had picked up the niggle during his match-winning innings of 87 off 45 balls against #DelhiCapitals on Tuesday and didn't keep wickets with substitute Shreevats Goswami replacing him. #IPL2020 \\n\\nhttps://t.co/kxn1wH5BfB\", truncated=False, display_text_range=[0, 234], entities={'hashtags': [{'text': 'DelhiCapitals', 'indices': [101, 115]}, {'text': 'IPL2020', 'indices': [200, 208]}], 'symbols': [], 'user_mentions': [], 'urls': [{'url': 'https://t.co/kxn1wH5BfB', 'expanded_url': 'https://www.firstpost.com/firstcricket/sports-news/ipl-2020-wriddhiman-sahas-groin-injury-not-serious-but-srh-likely-to-wait-and-watch-ahead-of-rcb-game-8960001.html', 'display_url': 'firstpost.com/firstcricket/s…', 'indices': [211, 234]}]}, metadata={'iso_language_code': 'en', 'result_type': 'recent'}, source='TweetDeck', source_url='https://about.twitter.com/products/tweetdeck', in_reply_to_status_id=None, in_reply_to_status_id_str=None, in_reply_to_user_id=None, in_reply_to_user_id_str=None, in_reply_to_screen_name=None, author=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 335891957, 'id_str': '335891957', 'name': 'Firstpost Sports', 'screen_name': 'FirstpostSports', 'location': 'India', 'description': 'Bringing you live updates, breaking news, opinions and photos from the world of sport.', 'url': 'http://t.co/XSaFXN4DBr', 'entities': {'url': {'urls': [{'url': 'http://t.co/XSaFXN4DBr', 'expanded_url': 'http://www.firstpost.com/category/sports', 'display_url': 'firstpost.com/category/sports', 'indices': [0, 22]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 441638, 'friends_count': 873, 'listed_count': 550, 'created_at': 'Fri Jul 15 12:15:40 +0000 2011', 'favourites_count': 6, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': True, 'statuses_count': 207984, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/2503138588/lc89nnbhz3tvpkztrxhe_normal.png', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/2503138588/lc89nnbhz3tvpkztrxhe_normal.png', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/335891957/1531981823', 'profile_link_color': '0084B4', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=335891957, id_str='335891957', name='Firstpost Sports', screen_name='FirstpostSports', location='India', description='Bringing you live updates, breaking news, opinions and photos from the world of sport.', url='http://t.co/XSaFXN4DBr', entities={'url': {'urls': [{'url': 'http://t.co/XSaFXN4DBr', 'expanded_url': 'http://www.firstpost.com/category/sports', 'display_url': 'firstpost.com/category/sports', 'indices': [0, 22]}]}, 'description': {'urls': []}}, protected=False, followers_count=441638, friends_count=873, listed_count=550, created_at=datetime.datetime(2011, 7, 15, 12, 15, 40), favourites_count=6, utc_offset=None, time_zone=None, geo_enabled=True, verified=True, statuses_count=207984, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='C0DEED', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/2503138588/lc89nnbhz3tvpkztrxhe_normal.png', profile_image_url_https='https://pbs.twimg.com/profile_images/2503138588/lc89nnbhz3tvpkztrxhe_normal.png', profile_banner_url='https://pbs.twimg.com/profile_banners/335891957/1531981823', profile_link_color='0084B4', profile_sidebar_border_color='FFFFFF', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), user=User(_api=<tweepy.api.API object at 0x0000021C4D04B460>, _json={'id': 335891957, 'id_str': '335891957', 'name': 'Firstpost Sports', 'screen_name': 'FirstpostSports', 'location': 'India', 'description': 'Bringing you live updates, breaking news, opinions and photos from the world of sport.', 'url': 'http://t.co/XSaFXN4DBr', 'entities': {'url': {'urls': [{'url': 'http://t.co/XSaFXN4DBr', 'expanded_url': 'http://www.firstpost.com/category/sports', 'display_url': 'firstpost.com/category/sports', 'indices': [0, 22]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 441638, 'friends_count': 873, 'listed_count': 550, 'created_at': 'Fri Jul 15 12:15:40 +0000 2011', 'favourites_count': 6, 'utc_offset': None, 'time_zone': None, 'geo_enabled': True, 'verified': True, 'statuses_count': 207984, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'C0DEED', 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/2503138588/lc89nnbhz3tvpkztrxhe_normal.png', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/2503138588/lc89nnbhz3tvpkztrxhe_normal.png', 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/335891957/1531981823', 'profile_link_color': '0084B4', 'profile_sidebar_border_color': 'FFFFFF', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': False, 'default_profile': False, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none'}, id=335891957, id_str='335891957', name='Firstpost Sports', screen_name='FirstpostSports', location='India', description='Bringing you live updates, breaking news, opinions and photos from the world of sport.', url='http://t.co/XSaFXN4DBr', entities={'url': {'urls': [{'url': 'http://t.co/XSaFXN4DBr', 'expanded_url': 'http://www.firstpost.com/category/sports', 'display_url': 'firstpost.com/category/sports', 'indices': [0, 22]}]}, 'description': {'urls': []}}, protected=False, followers_count=441638, friends_count=873, listed_count=550, created_at=datetime.datetime(2011, 7, 15, 12, 15, 40), favourites_count=6, utc_offset=None, time_zone=None, geo_enabled=True, verified=True, statuses_count=207984, lang=None, contributors_enabled=False, is_translator=False, is_translation_enabled=False, profile_background_color='C0DEED', profile_background_image_url='http://abs.twimg.com/images/themes/theme1/bg.png', profile_background_image_url_https='https://abs.twimg.com/images/themes/theme1/bg.png', profile_background_tile=False, profile_image_url='http://pbs.twimg.com/profile_images/2503138588/lc89nnbhz3tvpkztrxhe_normal.png', profile_image_url_https='https://pbs.twimg.com/profile_images/2503138588/lc89nnbhz3tvpkztrxhe_normal.png', profile_banner_url='https://pbs.twimg.com/profile_banners/335891957/1531981823', profile_link_color='0084B4', profile_sidebar_border_color='FFFFFF', profile_sidebar_fill_color='DDEEF6', profile_text_color='333333', profile_use_background_image=True, has_extended_profile=False, default_profile=False, default_profile_image=False, following=False, follow_request_sent=False, notifications=False, translator_type='none'), geo=None, coordinates=None, place=None, contributors=None, is_quote_status=False, retweet_count=0, favorite_count=5, favorited=False, retweeted=False, possibly_sensitive=False, lang='en') \n",
      "\n",
      ".....................................\n",
      "\n"
     ]
    }
   ],
   "source": [
    "Tweets = api.search( query , count=10 , lang='en' , exclude='retweets' , tweet_mode='extended' )\n",
    "# tweet_mode='extended'\n",
    "# tweet_mode='compat'\n",
    "\n",
    "for tweet in Tweets:\n",
    "    print(tweet,\"\\n\")\n",
    "    print(\".....................................\\n\")"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "Get the tweets and some Attributes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Empty DataFrame\n",
      "Columns: [Tweets, User, User_statuses_count, user_followers, User_location, User_verified, fav_count, rt_count, tweet_date]\n",
      "Index: []\n"
     ]
    }
   ],
   "source": [
    "df = pd.DataFrame(columns = ['Tweets' , 'User' , 'User_statuses_count' , \n",
    "                            'user_followers' , 'User_location' , 'User_verified' ,\n",
    "                            'fav_count' , 'rt_count' , 'tweet_date'] )\n",
    "print(df)\n",
    "# print(df.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def stream(data, file_name):\n",
    "    i = 0\n",
    "    for tweet in tweepy.Cursor(api.search, q=data, count=100, lang='en').items():\n",
    "        print(i, end='\\r')\n",
    "        df.loc[i, 'Tweets'] = tweet.text\n",
    "        df.loc[i, 'User'] = tweet.user.name\n",
    "        df.loc[i, 'User_statuses_count'] = tweet.user.statuses_count\n",
    "        df.loc[i, 'user_followers'] = tweet.user.followers_count\n",
    "        df.loc[i, 'User_location'] = tweet.user.location\n",
    "        df.loc[i, 'User_verified'] = tweet.user.verified\n",
    "        df.loc[i, 'fav_count'] = tweet.favorite_count\n",
    "        df.loc[i, 'rt_count'] = tweet.retweet_count\n",
    "        df.loc[i, 'tweet_date'] = tweet.created_at\n",
    "        df.to_excel('{}.xlsx'.format(file_name))\n",
    "        i = i+1\n",
    "        if i == 1000:\n",
    "            break\n",
    "        else:\n",
    "            pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "612\r"
     ]
    }
   ],
   "source": [
    "stream(data=[\"RCB winning IPL\"] , file_name='my_tweets')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Tweets</th>\n",
       "      <th>User</th>\n",
       "      <th>User_statuses_count</th>\n",
       "      <th>user_followers</th>\n",
       "      <th>User_location</th>\n",
       "      <th>User_verified</th>\n",
       "      <th>fav_count</th>\n",
       "      <th>rt_count</th>\n",
       "      <th>tweet_date</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>RCB have lacked with bowling combinations in t...</td>\n",
       "      <td>Moin Ali</td>\n",
       "      <td>419</td>\n",
       "      <td>459</td>\n",
       "      <td>Bengaluru South, India</td>\n",
       "      <td>False</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 12:55:16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Who will win today's IPL match MI vs RCB?\\nIt’...</td>\n",
       "      <td>Criconet</td>\n",
       "      <td>1965</td>\n",
       "      <td>84</td>\n",
       "      <td>Gurgaon, India</td>\n",
       "      <td>False</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 12:19:47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Both MI and RCB will be looking to secure thei...</td>\n",
       "      <td>Mumbai Live</td>\n",
       "      <td>24714</td>\n",
       "      <td>13507</td>\n",
       "      <td>Mumbai, India</td>\n",
       "      <td>False</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 12:08:08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>RT @Tro_Lee_: We #Mi fans consider only one te...</td>\n",
       "      <td>ꜱʜɪᴠᴀᴀᴹᴵ</td>\n",
       "      <td>38968</td>\n",
       "      <td>1066</td>\n",
       "      <td></td>\n",
       "      <td>False</td>\n",
       "      <td>0</td>\n",
       "      <td>42</td>\n",
       "      <td>2020-10-28 12:07:30</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>MI vs RCB Dream11 Winning Team Prediction\\n\\nV...</td>\n",
       "      <td>Dream11Prediction</td>\n",
       "      <td>422</td>\n",
       "      <td>136</td>\n",
       "      <td></td>\n",
       "      <td>False</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 11:54:07</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              Tweets               User  \\\n",
       "0  RCB have lacked with bowling combinations in t...           Moin Ali   \n",
       "1  Who will win today's IPL match MI vs RCB?\\nIt’...           Criconet   \n",
       "2  Both MI and RCB will be looking to secure thei...        Mumbai Live   \n",
       "3  RT @Tro_Lee_: We #Mi fans consider only one te...           ꜱʜɪᴠᴀᴀᴹᴵ   \n",
       "4  MI vs RCB Dream11 Winning Team Prediction\\n\\nV...  Dream11Prediction   \n",
       "\n",
       "  User_statuses_count user_followers           User_location User_verified  \\\n",
       "0                 419            459  Bengaluru South, India         False   \n",
       "1                1965             84          Gurgaon, India         False   \n",
       "2               24714          13507           Mumbai, India         False   \n",
       "3               38968           1066                                 False   \n",
       "4                 422            136                                 False   \n",
       "\n",
       "  fav_count rt_count           tweet_date  \n",
       "0         0        0  2020-10-28 12:55:16  \n",
       "1         1        0  2020-10-28 12:19:47  \n",
       "2         3        0  2020-10-28 12:08:08  \n",
       "3         0       42  2020-10-28 12:07:30  \n",
       "4         1        0  2020-10-28 11:54:07  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "!pip install textblob"
   ]
  },
  {
   "cell_type": "raw",
   "metadata": {},
   "source": [
    "Sentiment(polarity, subjectivity)\n",
    "\n",
    "Polarity score: [-1 , +1]\n",
    "\n",
    "Subjectivity: [0.0 , 1.0] \n",
    "where 0.0 is very Objective and 1.0 is very Subjective."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "from textblob import TextBlob"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "def clean_tweet(tweet):\n",
    "    return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \\t])|(\\w+:\\/\\/\\S+)', ' ', tweet).split())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def analyze_sentiment(tweet):\n",
    "    analysis = TextBlob(tweet)\n",
    "    if analysis.sentiment.polarity > 0:\n",
    "        return 'Positive'\n",
    "    elif analysis.sentiment.polarity == 0:\n",
    "        return 'Neutral'\n",
    "    else:\n",
    "        return 'Negative'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['clean_tweet'] = df['Tweets'].apply(lambda x : clean_tweet(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Tweets</th>\n",
       "      <th>User</th>\n",
       "      <th>User_statuses_count</th>\n",
       "      <th>user_followers</th>\n",
       "      <th>User_location</th>\n",
       "      <th>User_verified</th>\n",
       "      <th>fav_count</th>\n",
       "      <th>rt_count</th>\n",
       "      <th>tweet_date</th>\n",
       "      <th>clean_tweet</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>RCB have lacked with bowling combinations in t...</td>\n",
       "      <td>Moin Ali</td>\n",
       "      <td>419</td>\n",
       "      <td>459</td>\n",
       "      <td>Bengaluru South, India</td>\n",
       "      <td>False</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 12:55:16</td>\n",
       "      <td>RCB have lacked with bowling combinations in t...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Who will win today's IPL match MI vs RCB?\\nIt’...</td>\n",
       "      <td>Criconet</td>\n",
       "      <td>1965</td>\n",
       "      <td>84</td>\n",
       "      <td>Gurgaon, India</td>\n",
       "      <td>False</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 12:19:47</td>\n",
       "      <td>Who will win today s IPL match MI vs RCB It s ...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Both MI and RCB will be looking to secure thei...</td>\n",
       "      <td>Mumbai Live</td>\n",
       "      <td>24714</td>\n",
       "      <td>13507</td>\n",
       "      <td>Mumbai, India</td>\n",
       "      <td>False</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 12:08:08</td>\n",
       "      <td>Both MI and RCB will be looking to secure thei...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>RT @Tro_Lee_: We #Mi fans consider only one te...</td>\n",
       "      <td>ꜱʜɪᴠᴀᴀᴹᴵ</td>\n",
       "      <td>38968</td>\n",
       "      <td>1066</td>\n",
       "      <td></td>\n",
       "      <td>False</td>\n",
       "      <td>0</td>\n",
       "      <td>42</td>\n",
       "      <td>2020-10-28 12:07:30</td>\n",
       "      <td>RT Lee We Mi fans consider only one team as ou...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>MI vs RCB Dream11 Winning Team Prediction\\n\\nV...</td>\n",
       "      <td>Dream11Prediction</td>\n",
       "      <td>422</td>\n",
       "      <td>136</td>\n",
       "      <td></td>\n",
       "      <td>False</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 11:54:07</td>\n",
       "      <td>MI vs RCB Dream11 Winning Team Prediction Visi...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              Tweets               User  \\\n",
       "0  RCB have lacked with bowling combinations in t...           Moin Ali   \n",
       "1  Who will win today's IPL match MI vs RCB?\\nIt’...           Criconet   \n",
       "2  Both MI and RCB will be looking to secure thei...        Mumbai Live   \n",
       "3  RT @Tro_Lee_: We #Mi fans consider only one te...           ꜱʜɪᴠᴀᴀᴹᴵ   \n",
       "4  MI vs RCB Dream11 Winning Team Prediction\\n\\nV...  Dream11Prediction   \n",
       "\n",
       "  User_statuses_count user_followers           User_location User_verified  \\\n",
       "0                 419            459  Bengaluru South, India         False   \n",
       "1                1965             84          Gurgaon, India         False   \n",
       "2               24714          13507           Mumbai, India         False   \n",
       "3               38968           1066                                 False   \n",
       "4                 422            136                                 False   \n",
       "\n",
       "  fav_count rt_count           tweet_date  \\\n",
       "0         0        0  2020-10-28 12:55:16   \n",
       "1         1        0  2020-10-28 12:19:47   \n",
       "2         3        0  2020-10-28 12:08:08   \n",
       "3         0       42  2020-10-28 12:07:30   \n",
       "4         1        0  2020-10-28 11:54:07   \n",
       "\n",
       "                                         clean_tweet  \n",
       "0  RCB have lacked with bowling combinations in t...  \n",
       "1  Who will win today s IPL match MI vs RCB It s ...  \n",
       "2  Both MI and RCB will be looking to secure thei...  \n",
       "3  RT Lee We Mi fans consider only one team as ou...  \n",
       "4  MI vs RCB Dream11 Winning Team Prediction Visi...  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Tweets</th>\n",
       "      <th>User</th>\n",
       "      <th>User_statuses_count</th>\n",
       "      <th>user_followers</th>\n",
       "      <th>User_location</th>\n",
       "      <th>User_verified</th>\n",
       "      <th>fav_count</th>\n",
       "      <th>rt_count</th>\n",
       "      <th>tweet_date</th>\n",
       "      <th>clean_tweet</th>\n",
       "      <th>Sentiment</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>RCB have lacked with bowling combinations in t...</td>\n",
       "      <td>Moin Ali</td>\n",
       "      <td>419</td>\n",
       "      <td>459</td>\n",
       "      <td>Bengaluru South, India</td>\n",
       "      <td>False</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 12:55:16</td>\n",
       "      <td>RCB have lacked with bowling combinations in t...</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Who will win today's IPL match MI vs RCB?\\nIt’...</td>\n",
       "      <td>Criconet</td>\n",
       "      <td>1965</td>\n",
       "      <td>84</td>\n",
       "      <td>Gurgaon, India</td>\n",
       "      <td>False</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 12:19:47</td>\n",
       "      <td>Who will win today s IPL match MI vs RCB It s ...</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Both MI and RCB will be looking to secure thei...</td>\n",
       "      <td>Mumbai Live</td>\n",
       "      <td>24714</td>\n",
       "      <td>13507</td>\n",
       "      <td>Mumbai, India</td>\n",
       "      <td>False</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 12:08:08</td>\n",
       "      <td>Both MI and RCB will be looking to secure thei...</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>RT @Tro_Lee_: We #Mi fans consider only one te...</td>\n",
       "      <td>ꜱʜɪᴠᴀᴀᴹᴵ</td>\n",
       "      <td>38968</td>\n",
       "      <td>1066</td>\n",
       "      <td></td>\n",
       "      <td>False</td>\n",
       "      <td>0</td>\n",
       "      <td>42</td>\n",
       "      <td>2020-10-28 12:07:30</td>\n",
       "      <td>RT Lee We Mi fans consider only one team as ou...</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>MI vs RCB Dream11 Winning Team Prediction\\n\\nV...</td>\n",
       "      <td>Dream11Prediction</td>\n",
       "      <td>422</td>\n",
       "      <td>136</td>\n",
       "      <td></td>\n",
       "      <td>False</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2020-10-28 11:54:07</td>\n",
       "      <td>MI vs RCB Dream11 Winning Team Prediction Visi...</td>\n",
       "      <td>Positive</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                                              Tweets               User  \\\n",
       "0  RCB have lacked with bowling combinations in t...           Moin Ali   \n",
       "1  Who will win today's IPL match MI vs RCB?\\nIt’...           Criconet   \n",
       "2  Both MI and RCB will be looking to secure thei...        Mumbai Live   \n",
       "3  RT @Tro_Lee_: We #Mi fans consider only one te...           ꜱʜɪᴠᴀᴀᴹᴵ   \n",
       "4  MI vs RCB Dream11 Winning Team Prediction\\n\\nV...  Dream11Prediction   \n",
       "\n",
       "  User_statuses_count user_followers           User_location User_verified  \\\n",
       "0                 419            459  Bengaluru South, India         False   \n",
       "1                1965             84          Gurgaon, India         False   \n",
       "2               24714          13507           Mumbai, India         False   \n",
       "3               38968           1066                                 False   \n",
       "4                 422            136                                 False   \n",
       "\n",
       "  fav_count rt_count           tweet_date  \\\n",
       "0         0        0  2020-10-28 12:55:16   \n",
       "1         1        0  2020-10-28 12:19:47   \n",
       "2         3        0  2020-10-28 12:08:08   \n",
       "3         0       42  2020-10-28 12:07:30   \n",
       "4         1        0  2020-10-28 11:54:07   \n",
       "\n",
       "                                         clean_tweet Sentiment  \n",
       "0  RCB have lacked with bowling combinations in t...  Positive  \n",
       "1  Who will win today s IPL match MI vs RCB It s ...  Positive  \n",
       "2  Both MI and RCB will be looking to secure thei...  Positive  \n",
       "3  RT Lee We Mi fans consider only one team as ou...  Positive  \n",
       "4  MI vs RCB Dream11 Winning Team Prediction Visi...  Positive  "
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Sentiment'] = df['clean_tweet'].apply(lambda x : analyze_sentiment(x) )\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original tweet:\n",
      " Who will win today's IPL match MI vs RCB?\n",
      "It’s winning time!!! Take participation in our daily quiz and get a chanc… https://t.co/5WjEvWtIes\n",
      "\n",
      "Clean tweet:\n",
      " Who will win today s IPL match MI vs RCB It s winning time Take participation in our daily quiz and get a chanc\n",
      "\n",
      "Sentiment of the tweet:\n",
      " Positive\n"
     ]
    }
   ],
   "source": [
    "n = 1\n",
    "print(\"Original tweet:\\n\",df['Tweets'][n])\n",
    "print()\n",
    "print(\"Clean tweet:\\n\",df['clean_tweet'][n])\n",
    "print()\n",
    "print(\"Sentiment of the tweet:\\n\",df['Sentiment'][n])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original tweet:\n",
      " RT @Tro_Lee_: We #Mi fans consider only one team as our worthy opponent. And that team is out of the tournament. \n",
      "\n",
      "Even if you #Rcb guys en…\n",
      "\n",
      "Clean tweet:\n",
      " RT Lee We Mi fans consider only one team as our worthy opponent And that team is out of the tournament Even if you Rcb guys en\n",
      "\n",
      "Sentiment of the tweet:\n",
      " Positive\n"
     ]
    }
   ],
   "source": [
    "n = 20\n",
    "print(\"Original tweet:\\n\",df['Tweets'][n])\n",
    "print()\n",
    "print(\"Clean tweet:\\n\",df['clean_tweet'][n])\n",
    "print()\n",
    "print(\"Sentiment of the tweet:\\n\",df['Sentiment'][n])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Original tweet:\n",
      " RT @Trendulkar: Rohit Sharma is not in the Australia tour squad. So he is out of the IPL too then? So RCB is winning the final against MI?…\n",
      "\n",
      "Clean tweet:\n",
      " RT Rohit Sharma is not in the Australia tour squad So he is out of the IPL too then So RCB is winning the final against MI\n",
      "\n",
      "Sentiment of the tweet:\n",
      " Positive\n"
     ]
    }
   ],
   "source": [
    "n = 203\n",
    "print(\"Original tweet:\\n\",df['Tweets'][n])\n",
    "print()\n",
    "print(\"Clean tweet:\\n\",df['clean_tweet'][n])\n",
    "print()\n",
    "print(\"Sentiment of the tweet:\\n\",df['Sentiment'][n])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "532"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.Sentiment == 'Positive'].shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "46"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.Sentiment == 'Neutral'].shape[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "35"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[df.Sentiment == 'Negative'].shape[0]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Happy Learning"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
