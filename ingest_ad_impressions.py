{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "11e23a81-dca7-41db-9a65-15ac50a2828a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ingested Ad Impression: {'ad_creative_id': '123abc', 'user_id': 'user_1', 'timestamp': '2024-05-18T12:00:00Z', 'website': 'example.com'}\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "def ingest_ad_impressions(json_data):\n",
    "    data = json.loads(json_data)\n",
    "    print(\"Ingested Ad Impression:\", data)\n",
    "ad_impression_data = '{\"ad_creative_id\": \"123abc\" , \"user_id\": \"user_1\", \"timestamp\": \"2024-05-18T12:00:00Z\", \"website\": \"example.com\"}'\n",
    "ingest_ad_impressions(ad_impression_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2c7c48c-ca28-47b7-8898-515a387585af",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
