import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-oauth-callback',
  standalone: false,
  templateUrl: './oauth-callback.component.html',
  styleUrl: './oauth-callback.component.css'
})
export class OauthCallbackComponent implements OnInit{
  constructor(private route: ActivatedRoute,
              private authService: AuthService,
              private router: Router
  ){}

  ngOnInit(): void {
    this.route.queryParamMap.subscribe(params =>{
      const accessToken = params.get('access_token');
      const refreshToken = params.get('refresh_token');

      if (accessToken && refreshToken){
        this.authService.handleAuthCallback(accessToken, refreshToken);
        this.router.navigate(['/shoes']);
      }else{
        this.router.navigate(['/auth/login'])
      }
    })
  }
}
