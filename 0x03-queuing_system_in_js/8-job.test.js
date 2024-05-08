/**
 * Now that you created a job creator, let’s add tests:
 * Import the function createPushNotificationsJobs
 * Create a queue with Kue
 * Write a test suite for the createPushNotificationsJobs function:
 * Use queue.testMode to validate which jobs are inside the queue 
 * etc.
 */

import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();
const { expect } = require('chai');


describe('createPushNotificationsJobs', () => {
    beforeEach(() => {
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('should throw an error if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('string', queue)).to.throw('Jobs is not an array');
    });

    it('should create two new jobs to the queue', () => {
        const list = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 4562 to verify your account'
            }
        ];
        createPushNotificationsJobs(list, queue);
        expect(queue.testMode.jobs.length).to.equal(2);
    });

    it('should create a new job to the queue', () => {
        const list = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            }
        ];
        createPushNotificationsJobs(list, queue);
        expect(queue.testMode.jobs.length).to.equal(1);
    });
});
