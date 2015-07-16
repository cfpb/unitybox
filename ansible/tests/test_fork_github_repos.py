import imp
import os
from mock import patch
from nose.tools import assert_equals
ANSIBLE_DIR = os.path.dirname(os.path.dirname(__file__))
fork_github_repos = imp.load_source('fork_github_repos', os.path.join(ANSIBLE_DIR, 'library', 'fork_github_repos'))


def test_get_fork_url():
	# Arrange
	gh_api_url = 'https://api.github.com'
	user = 'some-user'
	repo = 'some-repo'

	# Action
	result = fork_github_repos.get_fork_url(gh_api_url, user, repo)

	# Assert
	assert_equals(result, "https://api.github.com/repos/some-user/some-repo")


def test_get_api_url():
	# Arrange
	gh_api_url = 'https://api.github.com'
	owner = 'some-user'
	repo_name = 'some-repo'

	# Action
	result = fork_github_repos.get_api_url(gh_api_url, owner, repo_name)

	# Assert
	assert_equals(result, "https://api.github.com/repos/some-user/some-repo/forks")	


@patch('requests.head')
def test_url_exists_200_expects_true(mock_head):
	# Arrange
	url = 'http://some-url.com'
	mock_head.return_value = type('response', (object,), {'status_code': 200})()

	# Action
	result = fork_github_repos.url_exists(url)

	# Assert
	assert_equals(result, True)


@patch('requests.head')
def test_url_exists_301_expects_true(mock_head):
	# Arrange
	url = 'http://some-url.com'
	mock_head.return_value = type('response', (object,), {'status_code': 301})()

	# Action
	result = fork_github_repos.url_exists(url)

	# Assert
	assert_equals(result, True)


@patch('requests.head')
def test_url_exists_404_expects_false(mock_head):
	# Arrange
	url = 'http://some-url.com'
	mock_head.return_value = type('response', (object,), {'status_code': 404})()

	# Action
	result = fork_github_repos.url_exists(url)

	# Assert
	assert_equals(result, False)




	