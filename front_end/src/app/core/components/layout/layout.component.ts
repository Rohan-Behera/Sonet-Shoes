import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../../../auth/services/auth.service';

@Component({
  selector: 'app-layout',
  standalone: false,
  templateUrl: './layout.component.html',
  styleUrl: './layout.component.css'
})
export class LayoutComponent {
  collapsed = false;
 
  navItems = [
    { label: 'Shoes',  icon: 'storefront',    route: '/shoes' },
    { label: 'Cart',   icon: 'shopping_cart',  route: '/cart' },
    { label: 'Orders', icon: 'receipt_long',   route: '/orders' },
  ];
 
  constructor(public router: Router, private authService: AuthService) {}
 
  isActive(route: string): boolean {
    return this.router.url.startsWith(route);
  }
 
  logout(): void {
    this.authService.logout();
  }
 
  toggleSidebar(): void {
    this.collapsed = !this.collapsed;
  }
}
