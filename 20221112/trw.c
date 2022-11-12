#include <stdio.h>

int max(int *arr, int size) {
    int m = -1; //  어차피 0과 양의 정수만 들어감을 알고 있어서.

    if (arr == NULL) return m;

    for (int i = 0; i < size; i++) {
        if (arr[i] > m) {
            m = arr[i];
        }
    }
    return m;
}

int trap(int *height, int heightSize) {
    int count = 0;

    for (int level = 0; level < max(height, heightSize); level++) {
        int first_block_index = -1;

        for (int index = 0; index < heightSize; index++) {
            if (height[index] > level) {
                if (first_block_index == -1) {
                    first_block_index = index;
                } else {
                    if ((index - first_block_index) > 1) {
                        count += index - first_block_index - 1;
                    }
                    first_block_index = index;
                }
            }
        }
    }

    return count;
}

int main() {
    int first_value[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    int first_result = trap(first_value, 12);

    int second_value[] = {4, 2, 0, 3, 2, 5};
    int second_result = trap(second_value, 6);

    printf("first result: %d\n", first_result);
    printf("second result: %d\n", second_result);
}