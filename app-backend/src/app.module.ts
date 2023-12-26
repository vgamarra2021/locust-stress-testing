import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { PostsModule } from './posts/posts.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { Post } from './posts/entities/post.entity';

@Module({
  imports: [TypeOrmModule.forRoot({
    type: 'mysql',
    host: 'mysql',
    port: 3306,
    username: 'root',
    password: 'blog_password',
    database: 'blog',
    synchronize: true,
    entities: [Post],
  }),
    PostsModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule { }
