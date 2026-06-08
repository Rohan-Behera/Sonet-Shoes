import { Component } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';
import { AuthFormsService } from '../../services/auth-forms.service';

@Component({
  selector: 'app-signup',
  standalone: false,
  templateUrl: './signup.component.html',
  styleUrl: './signup.component.css'
})
export class SignupComponent {
  signupForm !: FormGroup;
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
    this.signupForm = this.authformservice.signupForm();    
  }

  loginWithGoogle(){
    this.authService.loginWithGoogle();
  }

  get first_name() { return this.signupForm.get('first_name')!; }
  get last_name() { return this.signupForm.get('last_name')!; }
  get username() { return this.signupForm.get('username')!; }
  get email() { return this.signupForm.get('email')!; }
  get password() { return this.signupForm.get('password')!; }

  onSubmit(): void{
    if (this.signupForm.invalid){
      this.signupForm.markAllAsTouched();
      return;
    }
    this.loading = true;
    this.errorMessage = '';

    this.authService.signup(this.signupForm.value).subscribe({
      next: () => this.router.navigate(['/auth/login'], {
        queryParams: { registered : "true"}
      }),
      error: (err) => {
        this.loading = false;
        this.errorMessage = err.error?.detail || "Registration failed. Please try again."
      }
    })
  }

}
