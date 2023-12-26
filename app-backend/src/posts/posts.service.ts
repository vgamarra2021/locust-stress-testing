import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { Post } from './entities/post.entity';

@Injectable()
export class PostsService {
    constructor(
        @InjectRepository(Post)
        private postsRepository: Repository<Post>,
    ) { }

    async findAll(): Promise<Post[]> {
        return this.postsRepository.find();
    }

    async findOne(id: number): Promise<Post> {
        return this.postsRepository.findOne({ where: { id } });
    }

    async create(postData: Post): Promise<Post> {
        return this.postsRepository.save(postData);
    }

    async update(id: number, postData: Post): Promise<void> {
        await this.postsRepository.update(id, postData);
    }

    async remove(id: number): Promise<void> {
        await this.postsRepository.delete(id);
    }
}
