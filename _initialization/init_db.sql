-- =========================
-- users
-- =========================
CREATE TABLE IF NOT EXISTS users (
    id int4 GENERATED ALWAYS AS IDENTITY(
        INCREMENT BY 1
        MINVALUE 1
        MAXVALUE 2147483647
        START 1
        CACHE 1
        NO CYCLE
    ) NOT NULL,
    username varchar(30) NOT NULL,
    "password" varchar(255) NOT NULL,
    "name" varchar(30) NULL,
    age int4 NULL,
    address varchar(100) NULL,
    note varchar(500) NULL,
    email varchar(100) NULL,
    phone varchar(30) NULL,
    "role" varchar(30) DEFAULT 'user'::character varying NOT NULL,
    CONSTRAINT users_age_check CHECK (age >= 0),
    CONSTRAINT users_email_key UNIQUE (email),
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_username_key UNIQUE (username)
);

-- =========================
-- agents
-- =========================
CREATE TABLE IF NOT EXISTS agents (
    id serial4 NOT NULL,
    "name" varchar(30) NULL,
    email varchar(100) NULL,
    phone varchar(30) NULL,
    state varchar(30) DEFAULT 'active'::character varying NULL,
    CONSTRAINT agents_pkey PRIMARY KEY (id)
);

INSERT INTO agents (id, name, email, phone, state) VALUES
(1, 'Expedia', 'expedia@test.com', '2000000001', 'active'),
(2, 'Booking.com', 'booking@test.com', '2000000002', 'active'),
(3, 'TripAdvisor', 'tripadvisor@test.com', '2000000003', 'active'),
(4, 'Kayak', 'kayak@test.com', '2000000004', 'active'),
(5, 'Priceline', 'priceline@test.com', '2000000005', 'active'),
(6, 'Agoda', 'agoda@test.com', '2000000006', 'active'),
(7, 'Travelocity', 'travelocity@test.com', '2000000007', 'active'),
(8, 'Orbitz', 'orbitz@test.com', '2000000008', 'active'),
(9, 'CheapTickets', 'cheaptickets@test.com', '2000000009', 'active'),
(10, 'Hotwire', 'hotwire@test.com', '2000000010', 'active'),
(11, 'Airbnb', 'airbnb@test.com', '2000000011', 'active'),
(12, 'Turo', 'turo@test.com', '2000000012', 'active'),
(13, 'Hopper', 'hopper@test.com', '2000000013', 'active'),
(14, 'Skyscanner', 'skyscanner@test.com', '2000000014', 'active'),
(15, 'Trivago', 'trivago@test.com', '2000000015', 'active'),
(16, 'MakeMyTrip', 'makemytrip@test.com', '2000000016', 'active'),
(17, 'Ctrip', 'ctrip@test.com', '2000000017', 'active'),
(18, 'Traveloka', 'traveloka@test.com', '2000000018', 'active'),
(19, 'Lastminute', 'lastminute@test.com', '2000000019', 'active'),
(20, 'Cleartrip', 'cleartrip@test.com', '2000000020', 'active')
ON CONFLICT (id) DO NOTHING;

SELECT setval(
    pg_get_serial_sequence('agents', 'id'),
    COALESCE((SELECT MAX(id) FROM agents), 1),
    true
);

-- =========================
-- hotels
-- =========================
CREATE TABLE IF NOT EXISTS hotels (
    id serial4 NOT NULL,
    "name" varchar(255) NOT NULL,
    latitude float8 NULL,
    longitude float8 NULL,
    third_party_id int4 NOT NULL,
    review_score float8 NULL,
    review_score_word varchar(50) NULL,
    review_count int4 NULL,
    property_class int4 NULL,
    main_photo varchar(500) NULL,
    sub_photo_1 varchar(500) NULL,
    sub_photo_2 varchar(500) NULL,
    sub_photo_3 varchar(500) NULL,
    CONSTRAINT hotels_pkey PRIMARY KEY (id),
    CONSTRAINT uq_hotels_hotel_id UNIQUE (third_party_id)
);

-- =========================
-- flights
-- =========================
CREATE TABLE IF NOT EXISTS flights (
    id serial4 NOT NULL,
    departure_time timestamp NULL,
    arrival_time timestamp NULL,
    "token" text NULL,
    airline_name varchar(100) NULL,
    airline_code varchar(10) NULL,
    airline_logo text NULL,
    departure_airport varchar(10) NULL,
    departure_city varchar(100) NULL,
    arrival_airport varchar(10) NULL,
    arrival_city varchar(100) NULL,
    duration_seconds int4 NULL,
    stops int4 NULL,
    CONSTRAINT flights_pkey PRIMARY KEY (id)
);

-- =========================
-- attractions
-- =========================
CREATE TABLE IF NOT EXISTS attractions (
    id serial4 NOT NULL,
    third_party_id varchar(100) NOT NULL,
    slug varchar(255) NULL,
    "name" varchar(255) NOT NULL,
    description text NULL,
    short_description text NULL,
    "operator" varchar(255) NULL,
    city varchar(100) NULL,
    departure_address varchar(255) NULL,
    arrival_address varchar(255) NULL,
    free_cancellation bool NULL,
    primary_photo varchar(500) NULL,
    sub_photo_1 varchar(500) NULL,
    sub_photo_2 varchar(500) NULL,
    sub_photo_3 varchar(500) NULL,
    languages text NULL,
    whats_included text NULL,
    not_included text NULL,
    CONSTRAINT attractions_pkey PRIMARY KEY (id),
    CONSTRAINT attractions_attraction_id_key UNIQUE (third_party_id)
);

-- =========================
-- hotel_bookings
-- =========================
CREATE TABLE IF NOT EXISTS hotel_bookings (
    id serial4 NOT NULL,
    owner_id int4 NOT NULL,
    hotel_id int4 NOT NULL,
    agent_id int4 NOT NULL,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP NULL,
    checkin_date date NOT NULL,
    checkout_date date NOT NULL,
    price numeric(10, 2) NULL,
    state varchar(30) DEFAULT 'booked'::character varying NULL,
    currency varchar(10) NOT NULL,
    CONSTRAINT hotel_bookings_pkey PRIMARY KEY (id),
    CONSTRAINT fk_hotel_booking_users FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_hotel_booking_hotels FOREIGN KEY (hotel_id) REFERENCES hotels(id) ON DELETE CASCADE,
    CONSTRAINT fk_hotel_booking_agents FOREIGN KEY (agent_id) REFERENCES agents(id) ON DELETE CASCADE
);

-- =========================
-- flight_bookings
-- =========================
CREATE TABLE IF NOT EXISTS flight_bookings (
    id serial4 NOT NULL,
    owner_id int4 NOT NULL,
    flight_id int4 NOT NULL,
    agent_id int4 NOT NULL,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP NULL,
    cabin_class varchar(20) NULL,
    price numeric(10, 2) NULL,
    adult int4 DEFAULT 0 NULL,
    children varchar(50) DEFAULT '0' NULL,
    state varchar(20) DEFAULT 'booked'::character varying NULL,
    currency varchar(10) NOT NULL,
    CONSTRAINT flight_bookings_pkey PRIMARY KEY (id),
    CONSTRAINT fk_flight_booking_users FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_flight_booking_flights FOREIGN KEY (flight_id) REFERENCES flights(id) ON DELETE CASCADE,
    CONSTRAINT fk_flight_booking_agents FOREIGN KEY (agent_id) REFERENCES agents(id) ON DELETE CASCADE
);

-- =========================
-- attraction_bookings
-- =========================
CREATE TABLE IF NOT EXISTS attraction_bookings (
    id serial4 NOT NULL,
    owner_id int4 NOT NULL,
    attraction_id int4 NOT NULL,
    agent_id int4 NOT NULL,
    time_slot_id varchar(150) NULL,
    offer_id varchar(100) NULL,
    offer_item_id varchar(100) NULL,
    start_time timestamp NULL,
    "language" varchar(20) NULL,
    price numeric(10, 2) NULL,
    currency varchar(10) NOT NULL,
    state varchar(30) DEFAULT 'booked'::character varying NULL,
    created_at timestamp DEFAULT CURRENT_TIMESTAMP NULL,
    CONSTRAINT attraction_bookings_pkey PRIMARY KEY (id),
    CONSTRAINT fk_attraction_booking_users FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_attraction_booking_attractions FOREIGN KEY (attraction_id) REFERENCES attractions(id) ON DELETE CASCADE,
    CONSTRAINT fk_attraction_booking_agents FOREIGN KEY (agent_id) REFERENCES agents(id) ON DELETE CASCADE
);