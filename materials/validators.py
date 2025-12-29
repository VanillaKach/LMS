from django.core.exceptions import ValidationError
import re

def validate_youtube_link(value):
    """
    Валидатор для проверки, что ссылка ведёт на YouTube
    """
    pattern = r'^https?://(www\.)?youtube\.com/watch\?v=[\w-]+(|&[\w=&%]*)$'
    if not re.match(pattern, value):
        raise ValidationError('Ссылка должна вести на YouTube.')
