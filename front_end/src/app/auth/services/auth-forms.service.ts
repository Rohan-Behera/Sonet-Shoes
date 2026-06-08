import { Injectable } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';

@Injectable({
  providedIn: 'root'
})
export class AuthFormsService {

  constructor(private formbuilder : FormBuilder) { }


  signupForm(){
    let form = this.formbuilder.group({
      first_name: ['', [Validators.required, Validators.minLength(2)]],
      last_name:  ['', [Validators.required, Validators.minLength(2)]],
      username:   ['', [Validators.required, Validators.minLength(3), Validators.pattern(/^\S+$/)]],
      email:      ['', [Validators.required, Validators.email]],
      password:   ['', [Validators.required, Validators.minLength(6)]]
    });
    return form;
  }

  loginForm(){
    let form = this.formbuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]]
    });
    return form;
  }
}
