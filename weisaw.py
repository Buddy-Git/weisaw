from util.slack_user import SlackUser
from slash import apis
def lambda_handler(event, context):
    try:
        # ToDo: extract user details before performing anything
        # g.user_id = request.form.get('user_id')
        # g.channel_id = request.form['channel_id']
        # g.team_id = request.form['team_id']
        # # g.enterprise_id = request.form['enterprise_id']
        # g.user_name = request.form['user_name']
        # g.response_url = request.form['response_url']
        user = SlackUser(user_info="")
        action = event["body"]["action"]

        if action == "hello":
            apis.slack_greet()

        pass
    except Exception as ex:
        pass
