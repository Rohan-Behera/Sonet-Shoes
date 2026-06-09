import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { withInterceptors, provideHttpClient } from '@angular/common/http';
import { jwtInterceptor } from './auth/services/jwt.interceptor';
import { AuthModule } from './auth/auth.module';
import { CoreModules } from './core/core.module';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    AuthModule,
    CoreModules
  ],
  providers: [
    provideHttpClient(
      withInterceptors([jwtInterceptor])
    )
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
