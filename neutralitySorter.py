import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 \
  as Features

natural_language_understanding = NaturalLanguageUnderstandingV1(
  username="0f373726-b38f-4408-813b-70bffbdc8617",
  password="0P37DJy3PgNu",
  version="2017-02-27")

def emotionRank(url):
response = natural_language_understanding.analyze(
  url=url,
  features=[
    Features.Emotion(
    ),
  ]
)
return
