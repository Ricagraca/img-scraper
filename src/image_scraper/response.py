from dataclasses import dataclass
from urllib.parse import urlparse
import dacite

@dataclass
class Response:
    url: str
    mimeType: str
    
@dataclass
class Parameters:
    response: Response
    
@dataclass
class Event:
    params: Parameters

def convert(data) -> Event:
    dat: Event = dacite.from_dict(Event, data)
    return dat

def get_image_url(event: Event) -> str:
    try:
        parsedEvent = convert(event)
    except:
        return ''
    
    [type, _] = parsedEvent.params.response.mimeType.split('/')
    if type != 'image':
        return ''
                    
    if parsedEvent.params.response.url.find("images?q=tbn:") < 0:
        return ''
    
    parsed_uri = urlparse(parsedEvent.params.response.url)
    if parsed_uri.scheme != "http" and parsed_uri.scheme != "https":
        return ''
    
    return parsedEvent.params.response.url