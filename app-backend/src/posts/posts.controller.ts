import { Controller, Get, Post as PostMethod, Put, Delete, Body, Param } from '@nestjs/common';
import { PostsService } from './posts.service';
import { Post } from './entities/post.entity';

@Controller('posts')
export class PostsController {
    constructor(private postsService: PostsService) { }

    @Get()
    getAll(): Promise<Post[]> {
        return this.postsService.findAll();
    }

    @Get(':id')
    getOne(@Param('id') id: number): Promise<Post> {
        return this.postsService.findOne(id);
    }

    @PostMethod()
    create(@Body() postData: Post): Promise<Post> {
        console.log(`Data received : ${JSON.stringify(postData)}`)
        return this.postsService.create(postData);
    }

    @Put(':id')
    update(@Param('id') id: number, @Body() postData: Post): Promise<void> {
        return this.postsService.update(id, postData);
    }

    @Delete(':id')
    delete(@Param('id') id: number): Promise<void> {
        return this.postsService.remove(id);
    }
}
