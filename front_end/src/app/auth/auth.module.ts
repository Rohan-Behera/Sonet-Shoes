import { NgModule } from "@angular/core";
import { RouterModule, Routes } from "@angular/router";
import { LoginComponent } from "./components/login/login.component";
import { SignupComponent } from "./components/signup/signup.component";
import { OauthCallbackComponent } from "./components/oauth-callback/oauth-callback.component";
import { CommonModule } from "@angular/common";
import { ReactiveFormsModule } from "@angular/forms";
import { guestGuard } from "./services/auth.guard";
import { MatIconModule } from "@angular/material/icon";


const routes: Routes=[
    {
        path: '', redirectTo: 'login', pathMatch:'full'
    },
    {
        path: 'login', component: LoginComponent, canActivate: [guestGuard]
    },
    {
        path: 'signup', component: SignupComponent, canActivate: [guestGuard]
    },
    {
        path: 'callback', component: OauthCallbackComponent
    },
]

@NgModule({
    declarations:[
        LoginComponent,
        SignupComponent,
        OauthCallbackComponent
    ],
    imports:[
        CommonModule,
        ReactiveFormsModule,
        MatIconModule,
        RouterModule.forChild(routes)
    ]
})

export class AuthModule{}