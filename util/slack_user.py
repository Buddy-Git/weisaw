class SlackUser:
    def __init__(self, user_info):
        self.user_id = user_info['user_id']
        self.channel_id = user_info['channel_id']
        self.team_id = user_info['team_id']
        # self.enterprise_id = user_info['enterprise_id']
        self.user_name = user_info['user_name']
        self.response_url = user_info['response_url']
