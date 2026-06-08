export interface SignupPayload {
  first_name: string;
  last_name: string;
  username: string;
  email: string;
  password: string;
}

export interface LoginPayload {
  email: string;
  password: string;
}

export interface UserResponse {
  email: string;
  uid: string;
}

export interface LoginResponse {
  message: string;
  access_token: string;
  refresh_token: string;
  user: UserResponse;
}

export interface TokenDetails {
  user_details: {
    email: string;
    user_uid: string;
  };
  exp: number;
  type: string;
  refresh: boolean;
  jti: string;
}

export interface AuthResponse {
  access_token: string;
  refresh_token: string;
  user: any;
}