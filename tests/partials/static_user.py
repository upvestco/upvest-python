import uuid

from .client_instance import create_oauth_client, create_tenancy_client


"""
Create a single user in a known state with an expected number of wallets and
transactions that can be used in multiple tests
"""


def _make_static_user():
    # make a user with 2 wallets both containing 5 transactions
    username = f"upvest_test_static_{uuid.uuid4()}"
    tenancy_instance = create_tenancy_client()
    user = tenancy_instance.users.create(username, "secret")

    clientele = create_oauth_client(user.username, "secret")
    clientele.wallets.create("a3c18f74-935e-5d75-bd3c-ce0fb5464414", "secret")  # BTC
    clientele.wallets.create("deaaa6bf-d944-57fa-8ec4-2dd45d1f5d3f", "secret")

    return user


static_user = _make_static_user()
# single user to use across multiple tests
