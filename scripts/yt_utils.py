from typing import Dict, List, Any

def parse_comment(snippet: Dict[str, Any], 
                  top_level_comment: Dict[str, Any], 
                  replies: Dict[str, Any]) -> Dict[str, Any]:
    """
    Parse a single comment and return its data.

    Args:
        snippet (dict): The snippet containing comment details.
        top_level_comment (dict): The top-level comment snippet.
        replies (dict): The replies associated with the comment.

    Returns:
        dict: A dictionary containing the parsed comment data.
    """
    return {
        'channelId': snippet.get('channelId'),
        'videoId': snippet.get('videoId'),
        'commentId': top_level_comment.get('id'),  # Check if 'id' exists
        'textDisplay': top_level_comment.get('textDisplay'),
        'textOriginal': top_level_comment.get('textOriginal'),
        'authorDisplayName': top_level_comment.get('authorDisplayName'),
        'authorProfileImageUrl': top_level_comment.get('authorProfileImageUrl'),
        'authorChannelUrl': top_level_comment.get('authorChannelUrl'),
        'authorChannelId': top_level_comment.get('authorChannelId', {}).get('value'),  # Check if 'value' exists
        'canRate': top_level_comment.get('canRate'),
        'viewerRating': top_level_comment.get('viewerRating'),
        'likeCount': top_level_comment.get('likeCount'),
        'publishedAt': top_level_comment.get('publishedAt'),
        'updatedAt': top_level_comment.get('updatedAt'),
        'canReply': snippet.get('canReply'),
        'totalReplyCount': snippet.get('totalReplyCount'),
        'isPublic': snippet.get('isPublic'),
        'replies': replies
    }


def extract_comments(response: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Extract comments from the YouTube response.

    Args:
        response (dict): The API response containing items.

    Returns:
        list: A list of processed comment data.
    """
    data = []
    
    for item in response.get('items', []):
        snippet = item.get('snippet', {})
        top_level_comment = snippet.get('topLevelComment', {}).get('snippet', {})
        
        comment_replies = item.get('replies', {})
        
        comment_data = parse_comment(snippet, top_level_comment, comment_replies)
        data.append(comment_data)
    
    return data
