import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable, tap } from 'rxjs';
import { AuthResponse, LoginPayload, SignupPayload } from '../models/auth.models';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private readonly API = 'http://localhost:8000';

  constructor(private http: HttpClient, private router: Router) { }

  signup(payload: SignupPayload): Observable<any> {
    return this.http.post(`${this.API}/auth/signup`, payload)
  }

 login(payload: LoginPayload): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(`${this.API}/auth/login`, payload).pipe(
      tap((res) => {
        this.saveSession(res.access_token, res.refresh_token, res.user);
      })
    );
  }

  loginWithGoogle(): void {
    window.location.href = `${this.API}/oauth/google`;
  }

  handleAuthCallback(accessToken: string, refreshToken: string){
    localStorage.setItem('access_token', accessToken);
    localStorage.setItem('refresh_token', refreshToken);
  }

  logout(): void {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('user');
    this.router.navigate(['/auth/login']);
  }

  isLoggedIn(): boolean{
    return !!localStorage.getItem('access_token');
  }

  getAccessToken(): string | null {
    return localStorage.getItem('access_token');
  }


  private saveSession(accessToken: string, refreshToken: string, user?: any): void {
    localStorage.setItem('access_token', accessToken);
    localStorage.setItem('refresh_token', refreshToken);
    if (user) {
      localStorage.setItem('user', JSON.stringify(user));
    }
  }
}
