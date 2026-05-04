export interface HotelSearchResult {
  hotel_id: number;
  name: string;
  review_score: number;
  review_score_word: string;
  review_count: number;
  property_class: number;
  latitude: number;
  longitude: number;
  checkin_date: string;
  checkout_date: string;
  checkin_from_time: string;
  checkin_until_time: string;
  checkout_from_time: string;
  checkout_until_time: string;
  gross_price: number;
  excluded_price: number;
  main_photo: string;
  photo_urls: string[];
}
