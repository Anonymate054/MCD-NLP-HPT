from typing import Dict, List, Any
import pandas as pd
import json

def parse_comment(snippet: Dict[str, Any], 
                  top_level_comment: Dict[str, Any], 
                  replies: Dict[str, Any],
                  comment_id) -> Dict[str, Any]:
    """
    Parse a single comment and return its data.

    Args:
        snippet (dict): The snippet containing comment details.
        top_level_comment (dict): The top-level comment snippet.
        replies (dict): The replies associated with the comment.
        comment_id (str): The ID of the comment.

    Returns:
        dict: A dictionary containing the parsed comment data.
    """
    return {
        'channelId': snippet.get('channelId'),
        'videoId': snippet.get('videoId'),
        'commentId': comment_id,
        'textDisplay': top_level_comment.get('textDisplay'),
        'textOriginal': top_level_comment.get('textOriginal'),
        'authorDisplayName': top_level_comment.get('authorDisplayName'),
        'authorProfileImageUrl': top_level_comment.get('authorProfileImageUrl'),
        'authorChannelUrl': top_level_comment.get('authorChannelUrl'),
        'authorChannelId': top_level_comment.get('authorChannelId', {}).get('value'),
        'canRate': top_level_comment.get('canRate'),
        'viewerRating': top_level_comment.get('viewerRating'),
        'likeCount': top_level_comment.get('likeCount'),
        'publishedAt': top_level_comment.get('publishedAt'),
        'updatedAt': top_level_comment.get('updatedAt'),
        'canReply': snippet.get('canReply'),
        'totalReplyCount': snippet.get('totalReplyCount'),
        'isPublic': snippet.get('isPublic'),
        'replies': json.dumps(replies, ensure_ascii=True)  # Use ensure_ascii=False for UTF-8
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
        comment_id = snippet.get('topLevelComment', {}).get('id', '')  # Corrección: usar el id del topLevelComment

        comment_replies = item.get('replies', {})
        
        comment_data = parse_comment(snippet, top_level_comment, comment_replies, comment_id)
        data.append(comment_data)
    
    return data

def getReplies(replies: Dict[str, Any]) -> pd.DataFrame:
    """
    Extract replies from the replies dictionary and return them as a DataFrame.

    Args:
        replies (dict): The dictionary containing replies.

    Returns:
        pd.DataFrame: A DataFrame with the extracted replies.
    """
    # Extraer la información de cada respuesta y almacenarla en una lista
    reply_data = []
    
    for reply in replies.get('comments', []):
        reply_snippet = reply.get('snippet', {})
        reply_id = reply.get('id', '')
        
        # Añadir la información de la respuesta a la lista
        reply_data.append({
            'replyId': reply_id,
            'textDisplay': reply_snippet.get('textDisplay'),
            'textOriginal': reply_snippet.get('textOriginal'),
            'authorDisplayName': reply_snippet.get('authorDisplayName'),
            'authorProfileImageUrl': reply_snippet.get('authorProfileImageUrl'),
            'authorChannelUrl': reply_snippet.get('authorChannelUrl'),
            'authorChannelId': reply_snippet.get('authorChannelId', {}).get('value'),
            'parentId': reply_snippet.get('parentId'),
            'canRate': reply_snippet.get('canRate'),
            'viewerRating': reply_snippet.get('viewerRating'),
            'likeCount': reply_snippet.get('likeCount'),
            'publishedAt': reply_snippet.get('publishedAt'),
            'updatedAt': reply_snippet.get('updatedAt'),
        })
    
    # Convertir la lista de respuestas en un DataFrame de pandas
    return pd.DataFrame(reply_data)

def parse_comments_v2(data: Dict[str, Any]) -> pd.DataFrame:
    # Asume que 'data' ya contiene el JSON cargado

    # Normalizamos la parte de 'items' y extraemos la información de 'topLevelComment.snippet'
    df_items = pd.json_normalize(
        data['items'],
        meta=[
            'id',  # id del comentario principal
            ['snippet', 'videoId'],
            ['snippet', 'channelId'],
            ['snippet', 'canReply'],
            ['snippet', 'totalReplyCount'],
            ['snippet', 'isPublic'],
            ['snippet', 'topLevelComment', 'id'],
            ['snippet', 'topLevelComment', 'snippet', 'authorDisplayName'],
            ['snippet', 'topLevelComment', 'snippet', 'textDisplay'],
            ['snippet', 'topLevelComment', 'snippet', 'likeCount'],
            ['snippet', 'topLevelComment', 'snippet', 'publishedAt'],
            ['snippet', 'topLevelComment', 'snippet', 'updatedAt']
        ],
        meta_prefix='snippet_',
        errors='ignore'
    )

    # Normalizar respuestas solo si 'replies' está presente
    replies_list = [
        item.get('replies', {}).get('comments', []) for item in data['items'] if 'replies' in item
    ]

    # Aplanar los comentarios dentro de 'replies.comments' si existen
    df_replies = pd.json_normalize(
        [comment for sublist in replies_list for comment in sublist],
        meta_prefix='snippet_',
        errors='ignore'
    )

    # Concatenar los DataFrames si es necesario
    df_combined = pd.concat([df_items, df_replies], ignore_index=True)

    # Visualizar el DataFrame resultante
    return df_combined, df_replies, df_items
 