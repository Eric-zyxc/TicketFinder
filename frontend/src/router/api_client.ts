const IDENTITY_SERVICE_URL = "http://127.0.0.1:8000/";
const TICKET_SERVICE_URL = "http://127.0.0.1:8001/";

export function identity_request(api_call: string) {
  return IDENTITY_SERVICE_URL + api_call;
}
export function ticket_request(api_call: string) {
  return TICKET_SERVICE_URL + api_call;
}
