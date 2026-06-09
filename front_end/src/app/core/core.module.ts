import { NgModule } from "@angular/core";
import { LayoutComponent } from "./components/layout/layout.component";
import { CommonModule } from "@angular/common";
import { RouterModule } from "@angular/router";
import { MatIconModule } from "@angular/material/icon";





@NgModule({
    declarations:[
        LayoutComponent
    ],
    imports:[
        CommonModule,
        RouterModule,
        MatIconModule
    ],
    exports:[
        LayoutComponent
    ]
})

export class CoreModules{}