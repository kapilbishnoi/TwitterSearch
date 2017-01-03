require 'tweetstream'

TweetStream.configure do |config|
  config.consumer_key       = 'aRQFyWoJfLp0tQ7H1XxuPZ6yf'
  config.consumer_secret    = 'ROrOrif6nMVLGhdiAMsTbxvtJTPYHdR8xeY3BOsVLqSDt9h9DM'
  config.oauth_token        = '194929190-oJ9PnQ25hj0scOtZE0QdqYwLMr2SjQNsVpzIjLop'
  config.oauth_token_secret = 'R9nhtdha7UMBgs2lBeTiGPhHuAh2moMdJBBJajUKS6LkU'
  config.auth_method        = :oauth
end

# Use 'track' to track a list of single-word keywords
TweetStream::Client.new.track('@PMOIndia') do |status|
  puts "#{status.text}"
end