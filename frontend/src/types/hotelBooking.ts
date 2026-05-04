export interface HotelBookingPayload {
  third_party_id: number;
  name: string;
  latitude: number;
  longitude: number;
  main_photo: string;
  sub_photo_1: string;
  sub_photo_2: string;
  sub_photo_3: string;
  review_score: number;
  review_score_word: string;
  review_count: number;
  property_class: number;
  owner_id: number;
  agent_id: number;
  checkin_date: string;
  checkout_date: string;
  price: number;
  currency: string;
  excluded_price: number;
}
