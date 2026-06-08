import { Component } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { AuthFormsService } from '../../services/auth-forms.service';

@Component({
  selector: 'app-login',
  standalone: false,
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  loginForm !: FormGroup;
  loading = false;
  errorMessage = '';
  showPassword = false;

  constructor(
    private authService: AuthService,
    private router: Router,
    private authformservice: AuthFormsService
  ) {
    this.buildForm()
  }

  buildForm(){
    this.loginForm = this.authformservice.loginForm();
  }

  get email() { return this.loginForm.get('email')!; }
  get password() { return this.loginForm.get('password')!; }


  onSubmit(): void {
    if (this.loginForm.invalid) {
      this.loginForm.markAllAsTouched();
      return;
    }
    this.loading = true;
    this.errorMessage = '';
 
    this.authService.login(this.loginForm.value).subscribe({
      next: () => this.router.navigate(['/shoes']),
      error: (err) => {
        this.loading = false;
        this.errorMessage = err.error?.detail || 'Invalid email or password.';
      }
    });
  }

  loginWithGoogle(): void {
    this.authService.loginWithGoogle();
  }

}
