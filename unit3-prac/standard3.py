"""
You are managing a social media platform and need to ensure that posts are properly formatted. 
Each post must have balanced and correctly nested tags, such as () for mentions, 
[] for hashtags, and {} for links. You are given a string representing a post's content, 
and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:
    Every opening tag has a corresponding closing tag of the same type.
    Tags are closed in the correct order.
"""
def is_valid_post_format(posts):
  stack = []
  open_tags = "([{"
  close_tags = ")]}"

  index = 0

  while index < len(posts):
    if posts[index] in open_tags:
        stack.append(posts[index])
    elif posts[index] in close_tags:
       if not stack:
          return False
       elif posts[index] == ")" and stack[-1] == "(":
          stack.pop()
       elif posts[index] == "]" and stack[-1] == "[":
          stack.pop()
       elif posts[index] == "}" and stack[-1] == "{":
          stack.pop()
    index +=1
  return not stack       
    
"""
Given a queue of comments represented as a list of strings, reverse the order using a stack.
"""
'''

def reverse_comments_queue(comments):
  result = []
  stack = []
  print(comments)
  for comment in comments:
    print(comment)
    stack.append(comment)

    print(stack)
    
    pass
'''
def reverse_comments_queue(comments):
  result = []
  stack = []
  for comment in comments:
     stack.append(comment)

  index = 0
  while index < len(comments):
     result.append(stack.pop())
     index += 1

  return result

"""
you want to highlight post titles that are symmetrical, meaning they read the same forwards and backwards when ignoring spaces, 
punctuation, and case. Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if 
the title is symmetrical.
"""
def is_symmetrical_title(title):
  title = title.replace(" ", "")
  title = title.lower()
  start = 0
  end = len(title) - 1

  while(end >= start):
     if title[start] == title[end]:
        start += 1
        end -= 1
     else:
      return False

  return True


"""
Given an integer array engagements sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
Modify given solution to use two-pointer technique
"""
def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)  # [0,0,0,...,0]  -- the length of input array
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result



def main():
    print("---P1---")
    print(is_valid_post_format("()"))
    print(is_valid_post_format("()[]{}")) 
    print(is_valid_post_format("(]"))

    print("---P2---")
    print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
    print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

    print("---P3---")
    print(is_symmetrical_title("A Santa at NASA"))
    print(is_symmetrical_title("Social Media"))
    
    print("---P4---")
    print(engagement_boost([-4, -1, 0, 3, 10]))
    print(engagement_boost([-7, -3, 2, 3, 11]))

    return None


if __name__ == "__main__":
    main()