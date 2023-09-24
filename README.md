# Algorithm
## ✏️ 23-2 아이덱스 알고리즘 스터디
인하대학교 산업경영공학과 컴퓨터 소모임 아이덱스에서 진행하는 알고리즘 스터디

### ✅ 참여방법
1. 이 저장소를 clone 한다.
```
git clone 'https://github.com/INHA-Idecs/Algorithm.git'
```
2. 생성된 원격 저장소에 자신의 소스코드를 올릴 폴더를 생성한다. (ex. '/seaniiio' )
- 자신의 폴더 아래에 PGS 폴더 만들고 거기서 진행
- /seaniiio/PGS

3. 폴더에 일단 아무 파일이나 생성하고 커밋 후 push한다.
```
git add .
git commit -m "seaniiio(자신의 폴더명) 폴더 생성"
git push origin
```
3. 개인 작업 진행을 위해 개인 branch를 판다.
```
git branch "브랜치명"
# git branch seaniiio
```
4. 자신의 branch로 이동한다.
```
git checkout "브랜치명"
# git checkout seaniiio
```
5. 생성된 폴더에 자신의 풀이가 담긴 소스코드를 업로드 한다.
- 우선, 변경사항을 확인한다.
```
git status 
```
- 자기가 푼 문제를 add한다.
```
git add 파일명
```
- 커밋한다
```
git commit -m "커밋메세지(아이디 등 + 문제번호 + solve)"
# git commit -m "seaniiio 2512 solve"
```
- push한다
```
git push origin "브랜치명"
# git push origin seaniiio
```
fatal: The current branch seaniiio has no upstream branch. 이런 에러가 뜨면 원격 저장소에 대한 기본 브랜치 설정을 해야합니다!
```
git push --set-upstream origin main
```
6. 문제를 모두 풀었으면 main 브랜치로 PR을 날리고 merge한다.


### ❗️규칙
- 일주일에 4문제씩 주제에 맞춰 모두 풀어온다.
- 스터디 당일 풀이할 문제를 랜덤으로 뽑는다.( 모든 풀이를 준비해와야겠죠 🔆 )
- 개인의 브랜치 혹은 폴더에서만 작업한다.

